from pathlib import Path
import textwrap


WORKDIR = Path(r"c:\Users\stari\AppData\Local\Python\pythoncore-3.14-64\phyton-workspace")
SOURCE = WORKDIR / "ducks_support_master_handoff.md"
TARGET = WORKDIR / "ducks_support_master_handoff.pdf"

PAGE_WIDTH = 612
PAGE_HEIGHT = 792
LEFT = 50
TOP = 50
BOTTOM = 50
FONT_SIZE = 10
LEADING = 14
MAX_CHARS = 92


def escape_pdf_text(text: str) -> str:
    return text.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")


def normalize_text(text: str) -> str:
    replacements = {
        "\u2019": "'",
        "\u2018": "'",
        "\u201c": '"',
        "\u201d": '"',
        "\u2013": "-",
        "\u2014": "-",
        "\u2026": "...",
        "\u00a0": " ",
    }
    for src, dst in replacements.items():
        text = text.replace(src, dst)
    return text.encode("latin-1", "replace").decode("latin-1")


def wrap_markdown(text: str):
    lines = []
    for raw in text.splitlines():
        line = normalize_text(raw.rstrip())
        stripped = line.strip()
        if not stripped:
            lines.append("")
            continue

        if stripped.startswith("#"):
            title = stripped.lstrip("#").strip().upper()
            lines.append(title)
            lines.append("")
            continue

        indent = ""
        bullet = ""
        content = line

        if stripped.startswith("- "):
            indent = "  "
            bullet = "- "
            content = stripped[2:]
        elif stripped[0].isdigit() and ". " in stripped[:4]:
            split = stripped.split(". ", 1)
            bullet = split[0] + ". "
            indent = " " * len(bullet)
            content = split[1]
        else:
            content = stripped

        width = MAX_CHARS - len(indent) - len(bullet)
        wrapped = textwrap.wrap(content, width=max(20, width)) or [""]
        for i, part in enumerate(wrapped):
            prefix = bullet if i == 0 else indent
            lines.append(prefix + part)
    return lines


def paginate(lines):
    usable_height = PAGE_HEIGHT - TOP - BOTTOM
    lines_per_page = usable_height // LEADING
    pages = []
    current = []
    for line in lines:
        current.append(line)
        if len(current) >= lines_per_page:
            pages.append(current)
            current = []
    if current:
        pages.append(current)
    return pages


def page_stream(lines):
    y = PAGE_HEIGHT - TOP
    parts = ["BT", f"/F1 {FONT_SIZE} Tf", f"{LEFT} {y} Td"]
    first = True
    for line in lines:
        text = escape_pdf_text(line)
        if first:
            parts.append(f"({text}) Tj")
            first = False
        else:
            parts.append(f"0 -{LEADING} Td")
            parts.append(f"({text}) Tj")
    parts.append("ET")
    return "\n".join(parts).encode("latin-1", "replace")


def build_pdf(pages):
    objects = []

    def add_object(data: bytes):
        objects.append(data)
        return len(objects)

    font_id = add_object(b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>")
    placeholder_pages_id = add_object(b"")
    page_ids = []

    for page in pages:
        stream = page_stream(page)
        content = (
            f"<< /Length {len(stream)} >>\nstream\n".encode("latin-1")
            + stream
            + b"\nendstream"
        )
        content_id = add_object(content)

        page_obj = (
            f"<< /Type /Page /Parent {placeholder_pages_id} 0 R /MediaBox [0 0 {PAGE_WIDTH} {PAGE_HEIGHT}] "
            f"/Resources << /Font << /F1 {font_id} 0 R >> >> /Contents {content_id} 0 R >>"
        ).encode("latin-1")
        page_id = add_object(page_obj)
        page_ids.append(page_id)

    kids = " ".join(f"{pid} 0 R" for pid in page_ids)
    pages_obj = f"<< /Type /Pages /Count {len(page_ids)} /Kids [{kids}] >>".encode("latin-1")
    objects[placeholder_pages_id - 1] = pages_obj

    catalog_id = add_object(
        f"<< /Type /Catalog /Pages {placeholder_pages_id} 0 R >>".encode("latin-1")
    )

    pdf = bytearray(b"%PDF-1.4\n%\xe2\xe3\xcf\xd3\n")
    offsets = [0]
    for i, obj in enumerate(objects, start=1):
        offsets.append(len(pdf))
        pdf.extend(f"{i} 0 obj\n".encode("latin-1"))
        pdf.extend(obj)
        pdf.extend(b"\nendobj\n")

    xref_start = len(pdf)
    pdf.extend(f"xref\n0 {len(objects) + 1}\n".encode("latin-1"))
    pdf.extend(b"0000000000 65535 f \n")
    for off in offsets[1:]:
        pdf.extend(f"{off:010d} 00000 n \n".encode("latin-1"))
    pdf.extend(
        (
            f"trailer\n<< /Size {len(objects) + 1} /Root {catalog_id} 0 R >>\n"
            f"startxref\n{xref_start}\n%%EOF\n"
        ).encode("latin-1")
    )
    return pdf


def main():
    text = SOURCE.read_text(encoding="utf-8")
    lines = wrap_markdown(text)
    pages = paginate(lines)
    pdf = build_pdf(pages)
    TARGET.write_bytes(pdf)
    print(TARGET)


if __name__ == "__main__":
    main()
