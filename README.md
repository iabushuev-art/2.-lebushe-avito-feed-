# Le Bushe — Avito Autoload Feed

XML-фид для автозагрузки объявлений в Avito (магазин Le Bushe, ID: `i369926028`).

## Использование

URL фида (после настройки GitHub Pages):
```
https://iabushuev-art.github.io/2.-lebushe-avito-feed-/avito.xml
```

Этот URL нужно указать в **Личном кабинете Авито → Автозагрузка** (один раз).

Avito автоматически забирает файл каждый час.

## Формат

Стандартный XML Avito v3 — см. [docs](https://developers.avito.ru/).

## Локальный запуск

```bash
python3 generate.py  # создаст avito.xml
```
