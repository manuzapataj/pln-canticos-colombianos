# Cánticos del fútbol colombiano | Procesamiento de lenguaje natural

Proyecto académico de **Procesamiento y Entendimiento del Lenguaje Natural** de la Universidad Nacional de Colombia. La primera fase construyó un corpus de cánticos asociados a los 20 clubes de la Liga BetPlay A de 2026, con reglas para verificar fuentes, preservar el lenguaje de los textos y documentar duplicados.

## Cuadernos

- [Entrega final de PLN](entregas/pln_cuatro_fases_final.ipynb) · preparación del corpus, diversidad léxica, TF-IDF y vectores contextuales, similitud, clasificación *zero-shot* y reconocimiento de entidades.
- [Resumen reproducible de la primera fase](analisis.ipynb) · controles de cobertura y duplicados con los datos agregados incluidos.

## Qué quedó en el corpus

- Se integraron **600 cánticos** de **17 de los 20 clubes**. La fecha de corte de esta primera fase fue el **1 de septiembre de 2026**.
- Las 610 capturas iniciales incluyeron 10 duplicados exactos. El control de calidad dejó 88 registros marcados para revisión manual, sin tratarlos automáticamente como duplicados.
- Los tres clubes sin textos recuperados aparecen con cero en la tabla de cobertura. Ese cero describe las fuentes consultadas.

![Cobertura de los clubes con más registros](figuras/cobertura.png)

## Método y reproducción

La integración conserva el texto fuente en el corpus de trabajo. La comparación utiliza una representación de revisión independiente, registra la procedencia y documenta los cambios de identidad de clubes. La [versión de portafolio](analisis.ipynb) permite reproducir los controles sobre las [tablas agregadas](datos/). Los conteos reflejan cobertura digital y no miden lo que siente una hinchada ni la prevalencia general de una temática.

Con los dos CSV del proyecto académico, el script vuelve a contar observaciones por club a partir de sus identificadores y nombres. La redistribución de letras completas requeriría verificar las condiciones de las fuentes.

```bash
python contar_cobertura.py canticos.csv clubes.csv --salida cobertura_local.csv
```

**Fuentes de la primera fase** FanChants y Barrabrava.net, según la bitácora del proyecto.

**Crédito** Trabajo académico de Manuela Zapata Jiménez y David Cardona Duque. El resumen describe la construcción del corpus y la entrega final documenta las cuatro fases.

**English summary.** An NLP data-curation case study on Colombian football chants, documenting corpus coverage, exact duplicates and cases flagged for manual review. The final notebook also covers text preparation, similarity, zero-shot classification and named entity recognition.
