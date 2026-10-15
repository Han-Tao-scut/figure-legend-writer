"""Validate the two installable skill folders without machine-specific paths."""
import ast
from pathlib import Path
import re
import sys
import yaml

ROOT = Path(__file__).resolve().parents[1]
NAMES = ('figure-draw', 'figure-legend-writer')


def validate(folder):
    content = (folder / 'SKILL.md').read_text(encoding='utf-8')
    match = re.match(r'^---\n(.*?)\n---\n', content, re.S)
    if not match:
        raise ValueError(f'{folder.name}: missing YAML frontmatter')
    meta = yaml.safe_load(match[1])
    if not isinstance(meta, dict) or meta.get('name') != folder.name:
        raise ValueError(f'{folder.name}: frontmatter name must match directory')
    description = meta.get('description')
    if not isinstance(description, str) or not description.strip():
        raise ValueError(f'{folder.name}: description is required')
    ui = yaml.safe_load((folder / 'agents/openai.yaml').read_text())['interface']
    if not 25 <= len(ui['short_description']) <= 64:
        raise ValueError(f'{folder.name}: UI description must have 25-64 characters')
    if '$' + folder.name not in ui['default_prompt']:
        raise ValueError(f'{folder.name}: default prompt must mention the skill')
    for path in folder.rglob('*'):
        if not path.is_file() or '__pycache__' in path.parts:
            continue
        if path.is_symlink():
            raise ValueError(f'{path}: symlinks are not included in these skills')
        if path.suffix == '.md':
            text = path.read_text(encoding='utf-8')
            if '[TODO:' in text:
                raise ValueError(f'{path}: unfinished scaffold')
            for target in re.findall(r'\]\(([^)]+)\)', text):
                if '://' in target or target.startswith('#'):
                    continue
                destination = (path.parent / target.split('#')[0]).resolve()
                if not destination.is_relative_to(folder.resolve()) or not destination.is_file():
                    raise ValueError(f'{path}: broken or outside reference {target}')
        elif path.suffix == '.py':
            ast.parse(path.read_text(encoding='utf-8'), filename=str(path))


def main():
    try:
        for name in NAMES:
            validate(ROOT / 'skills' / name)
            print(f'PASS: {name}')
    except (ValueError, KeyError, OSError, SyntaxError, yaml.YAMLError) as error:
        print(f'FAIL: {error}', file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
