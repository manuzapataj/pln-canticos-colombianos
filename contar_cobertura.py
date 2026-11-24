from argparse import ArgumentParser
from collections import Counter
import csv
from pathlib import Path


def count_by_club(corpus, clubs):
    with clubs.open(encoding='utf-8-sig', newline='') as stream:
        catalog = csv.DictReader(stream)
        if not {'club_id', 'nombre_corto'} <= set(catalog.fieldnames or []):
            raise ValueError('El catálogo requiere club_id y nombre_corto.')
        labels = {}
        for row in catalog:
            club = row['club_id']
            if not club or not row['nombre_corto'] or club in labels:
                raise ValueError('Cada club debe tener un identificador único y un nombre.')
            labels[club] = row['nombre_corto']

    with corpus.open(encoding='utf-8-sig', newline='') as stream:
        records = csv.DictReader(stream)
        if 'club_id' not in (records.fieldnames or []):
            raise ValueError('El corpus requiere la columna club_id.')
        counts = Counter(row['club_id'] for row in records)
    if not counts.keys() <= labels.keys():
        raise ValueError('Hay registros que no corresponden a un club del catálogo.')
    return sorted(((name, counts[club]) for club, name in labels.items()), key=lambda row: (-row[1], row[0]))


def main():
    parser = ArgumentParser(description='Recalcula la cobertura por club de un corpus ya integrado.')
    parser.add_argument('corpus', type=Path)
    parser.add_argument('clubes', type=Path)
    parser.add_argument('--salida', required=True, type=Path)
    args = parser.parse_args()
    coverage = count_by_club(args.corpus, args.clubes)
    with args.salida.open('w', encoding='utf-8', newline='') as stream:
        writer = csv.writer(stream)
        writer.writerow(('club', 'canticos_integrados'))
        writer.writerows(coverage)
    print(f'Cánticos integrados: {sum(count for _, count in coverage):,}; clubes del catálogo: {len(coverage)}')


if __name__ == '__main__':
    main()
