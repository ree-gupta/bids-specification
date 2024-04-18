import io

import markdown
import pandas as pd
from tabulate import tabulate


def fence(
    source: str,
    language: str,
    css_class: str,
    options: dict,
    md: markdown.Markdown,
    **kwargs,
) -> str:
    df = pd.read_csv(io.StringIO(source), sep="\t")
    md_table = tabulate(df, headers="keys", tablefmt="github", showindex=False)  # type: ignore
    return md.convert(md_table)
