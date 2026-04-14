import argparse
from pathlib import Path


def render_sql(input_sql_path: str, env: str) -> None:
    input_path = Path(input_sql_path)

    if not input_path.exists():
        raise FileNotFoundError(f"File not found: {input_path}")

    if input_path.suffix.lower() != ".sql":
        raise ValueError("Input file must be a .sql file")

    # Read original SQL
    sql_text = input_path.read_text(encoding="utf-8")

    # Replace {{env}} with provided env
    rendered_sql = sql_text.replace("{{env}}", env)

    # Create output filename: originalname_ENV.sql
    output_path = input_path.with_name(
        f"{input_path.stem}_{env}{input_path.suffix}"
    )

    # Write rendered SQL
    output_path.write_text(rendered_sql, encoding="utf-8")

    print(f"SQL rendered successfully:")
    print(f"   Input : {input_path}")
    print(f"   Output: {output_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Render SQL file by replacing {{env}} with a given environment"
    )

    parser.add_argument(
        "--input",
        required=True,
        help="Path to the input .sql file"
    )

    parser.add_argument(
        "--env",
        required=True,
        help="Environment name (e.g. DEV, STAGING, PROD)"
    )

    args = parser.parse_args()

    render_sql(args.input, args.env)
