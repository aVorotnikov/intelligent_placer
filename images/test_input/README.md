# Тестовые входные данные
# Описание формата
Каждый случай представляет из себя отдельную директорию. Её содержимое:
* sample.jpg - входное изображение
* explanation.jpg - объяснение входных данных
* polygon.txt - описание многоугольника
# Описание случаев
## [color_similar](color_similar)
Проверяется выделение объекта со схожим фону цветом и достаточным прямоугольником

*Output*: True
## [color_similar_too_big](color_similar_too_big)
Проверяется выделение объекта со схожим фону цветом и слишком малым прямоугольником

*Output*: False
## [rotation](rotation)
Проверяется поворот объекта

*Output*: True
## [bars_only](bars_only)
Проверяется выделение объектов, похожих на прямоугольники и описывающим прямоугольником

*Output*: True
## [bars_only_complex_border](bars_only_complex_border)
Проверяется выделение объектов, похожих на прямоугольники и сложным многоугольником в качестве границы

*Output*: True
## [circles_only](circles_only)
Проверяется выделение объектов, похожих на круги

*Output*: True
## [spinner_curves](spinner_curves)
Проверяется обработка сложной формы

*Output*: True
## [all_different](all_different)
Проверяется случай, когда все объекты разные и многоугольник достаточно большой

*Output*: True
## [all_different_too_big](all_different_too_big)
Проверяется случай, когда все объекты разные и мноугольник слишком мал

*Output*: True