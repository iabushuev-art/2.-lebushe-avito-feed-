"""
Avito Autoload Feed Generator for Le Bushe.
Генерирует XML-фид в формате Avito Autoload v4 из каталога товаров.

Использование:
    python3 generate.py

Результат: avito.xml в текущей директории.

Структура XML:
- <Ads target="Avito.ru" formatVersion="4">
- <Ad>
    - <Id> - уникальный идентификатор
    - <Category> - "Одежда, обувь, аксессуары" или "Детская одежда и обувь"
    - <GoodsType> - "Мужская одежда" | "Мужская обувь" | "Женская одежда" | "Женская обувь" | "Для мальчиков" | ...
    - <ApparelType> - "Кроссовки" | "Кеды" | "Туфли" | "Рубашки" (для категорий с подкатегориями)
    - <Apparel> - "Кофты и футболки" (для мужских толстовок)
    - <GoodsSubType> - "Толстовка" | "Худи" | "Рубашка" (подтип)
    - <Brand> - из справочника brendy_fashion.xml (Burberry, Olymp, Guess, Plein sport)
    - <Size> - из справочника: "50 (L)" для одежды, "43" для обуви
    - <Title>, <Description>, <Price>, <Condition>, etc.

Бренды (точные имена из справочника Avito):
    - Burberry → "Burberry"
    - OLYMP → "Olymp"
    - GUESS → "Guess"
    - PLEIN SPORT → "Plein sport"
"""

PRODUCTS = [
    # OLYMP LUXOR рубашка — категория Личные вещи > Мужская одежда > Рубашки
    {
        "sku": "52056",
        "category": "Одежда, обувь, аксессуары",
        "goods_type": "Мужская одежда",
        "apparel_type": "Рубашки",
        "title": "Рубашка мужская OLYMP LUXOR modern fit, р.L (large), хлопок 100%, отличное",
        "description": "Рубашка мужская OLYMP LUXOR modern fit, размер L (large). Классическая мужская рубашка от премиального немецкого бренда OLYMP. Силуэт modern fit — современная посадка между slim и regular. Цвет — голубой с мелкой повторяющейся клеткой (микро-узор из тёмно-синих и белых элементов). Контрастная отделка внутренней стороны воротника и манжет — однотонный голубой. Пуговицы белые. Нагрудный карман слева. Состав: 100% хлопок (Baumwolle/Cotton). Уход: машинная стирка при 40°. Код производителя: 1258|69|11. Артикул галереи: 52056. Состояние: б/у, в отличном виде — практически как новая. Без следов носки, потёртостей, пятен и других дефектов.",
        "price": 1990,
        "condition": "Отличное",
        "ad_type": "Товар приобретен на продажу",
        "brand": "Olymp",
        "color": "Голубой",
        "size": "50 (L)",
        "material": "хлопок",
        "address": "Москва, пр-т Маршала Жукова, 39к1",
        "images": [
            "https://avatars.mds.yandex.net/get-yastore/21580234/9vm2cphzkrgmnjsslfkkvwt6x8mbn8xf/orig",
            "https://avatars.mds.yandex.net/get-yastore/20493671/ztx4dwk4vhd8rt84p6rfsbvtmdp9p6l9/orig",
        ],
    },
    # Plein Sport кроссовки мужские — Кроссовки мужские
    {
        "sku": "00575",
        "category": "Одежда, обувь, аксессуары",
        "goods_type": "Мужская обувь",
        "apparel_type": "Кроссовки",
        "title": "Кроссовки Plein Sport Lo-Top, р.43, белый/чёрный, новые с биркой",
        "description": "Кроссовки мужские Plein Sport Lo-Top Sneakers, размер 43. Спортивные кроссовки от итальянского бренда Plein Sport (суббренд Philipp Plein). Линейка Sport — активный молодёжный стиль, сочетание streetwear и люкса. Силуэт Lo-Top — низкие кроссовки с массивной подошвой. Верх — текстиль (mesh) с кожаными вставками и большим логотипом PS. Подошва — массивная белая платформа. Цвет — белый с чёрными акцентами. Артикул производителя: SADS USC0611 STE003N. Артикул галереи: 00575. Состояние: новые, с биркой. Производство: MADE IN CHINA.",
        "price": 7990,
        "condition": "Новое с биркой",
        "ad_type": "Товар приобретен на продажу",
        "brand": "Plein sport",
        "color": "Белый",
        "size": "43",
        "material": "текстиль",
        "address": "Москва, пр-т Маршала Жукова, 39к1",
        "images": [
            "https://avatars.mds.yandex.net/get-yastore/21580234/9vm2cphzkrgmnjsslfkkvwt6x8mbn8xf/orig",
        ],
    },
    # Guess ESSENTIALS туфли женские
    {
        "sku": "00576",
        "category": "Одежда, обувь, аксессуары",
        "goods_type": "Женская обувь",
        "apparel_type": "Туфли",
        "title": "Туфли женские Guess ESSENTIALS, р.36, монограммный принт, новые с биркой",
        "description": "Туфли женские Guess ESSENTIALS, размер 36. Классические женские лодочки на каблуке от американского бренда Guess. Коллекция ESSENTIALS — базовая линейка бренда, фирменный паттерн 4G в монохромном исполнении. Силуэт — классические pointed-toe pumps на высокой шпильке. Верх — текстиль с фирменным монограммным узором Guess 4G. Каблук — высокая шпилька. Подкладка и стелька — натуральная кожа, логотип Guess на стельке. Размер EUR 36. Артикул галереи: 00576. Состояние: новые, с биркой.",
        "price": 2990,
        "condition": "Новое с биркой",
        "ad_type": "Товар приобретен на продажу",
        "brand": "Guess",
        "color": "Разноцветный",
        "size": "36",
        "material": "текстиль",
        "address": "Москва, пр-т Маршала Жукова, 39к1",
        "images": [
            "https://avatars.mds.yandex.net/get-yastore/21580234/9vm2cphzkrgmnjsslfkkvwt6x8mbn8xf/orig",
        ],
    },
    # Guess Sock Sneakers кеды женские — категория "Кроссовки и кеды"
    {
        "sku": "00579",
        "category": "Одежда, обувь, аксессуары",
        "goods_type": "Женская обувь",
        "apparel_type": "Кроссовки и кеды",
        "title": "Кеды Guess Sock Sneakers, р.39, чёрные с золотой лентой, отличное",
        "description": "Кеды (слипоны) женские Guess Sock Sneakers, размер 39. Женские высокие слипоны в стиле sport-chic от Guess. Силуэт — sock-style, высокий чулок из эластичного текстиля, надевается без шнурков. Верх — чёрный текстиль (стрейч), облегает щиколотку. Горловина отделана фирменной золотистой лентой с повторяющимся логотипом GUESS. Подошва — массивная белая платформа с резиновым рантом, GUESS тиснён на подошве. Размер EUR 39. Артикул галереи: 00579. Состояние: б/у, в отличном виде. Сезон: демисезон.",
        "price": 3990,
        "condition": "Отличное",
        "ad_type": "Товар приобретен на продажу",
        "brand": "Guess",
        "color": "Чёрный",
        "size": "39",
        "material": "текстиль",
        "address": "Москва, пр-т Маршала Жукова, 39к1",
        "images": [
            "https://avatars.mds.yandex.net/get-yastore/21580234/9vm2cphzkrgmnjsslfkkvwt6x8mbn8xf/orig",
        ],
    },
    # Burberry Knightsbridge толстовка — категория Мужская одежда > Кофты и футболки
    {
        "sku": "27349",
        "category": "Одежда, обувь, аксессуары",
        "goods_type": "Мужская одежда",
        "apparel": "Кофты и футболки",
        "goods_sub_type": "Толстовка",
        "title": "Толстовка Burberry Knightsbridge Octopus, унисекс, р.L, модал 100%, отличное",
        "description": "Толстовка (худи) Burberry Knightsbridge Octopus Print, размер L, унисекс. Лимитированная толстовка от Burberry из линейки Knightsbridge — капсульная коллекция к юбилею лондонского адреса Horseferry House SW1. Силуэт — классический худи с капюшоном на шнурках, кенгуру-карман, длинный рукав. Принт — крупная графика осьминога (коричнево-оранжевые щупальца с присосками). Факсимильный лейбл Burberry, Knightsbridge SW1, Kingdom, LONDON ENGLAND. Состав: 100% модал. Производство: Италия. Замеры (см): плечи 50, грудь 62, спинка 72, рукав от плеча 70, рукав от подмышки 53. Артикул галереи: 27349. Состояние: б/у, в отличном виде. Стиль: спорт-стрит.",
        "price": 18490,
        "condition": "Отличное",
        "ad_type": "Товар приобретен на продажу",
        "brand": "Burberry",
        "color": "Чёрный",
        "size": "50 (L)",
        "material": "модал",
        "address": "Москва, пр-т Маршала Жукова, 39к1",
        "images": [
            "https://avatars.mds.yandex.net/get-yastore/21580234/9vm2cphzkrgmnjsslfkkvwt6x8mbn8xf/orig",
        ],
    },
]


def xml_escape(text):
    """Экранируем XML-сущности."""
    return (str(text)
            .replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
            .replace('"', "&quot;")
            .replace("'", "&apos;"))


def generate_xml():
    """Генерирует XML-фид в формате Avito Autoload v4."""
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml += '<Ads target="Avito.ru" formatVersion="4">\n'

    for p in PRODUCTS:
        xml += '  <Ad>\n'
        xml += f'    <Id>{xml_escape(p["sku"])}</Id>\n'
        xml += f'    <Category>{xml_escape(p["category"])}</Category>\n'
        xml += f'    <GoodsType>{xml_escape(p["goods_type"])}</GoodsType>\n'
        if p.get("apparel_type"):
            xml += f'    <ApparelType>{xml_escape(p["apparel_type"])}</ApparelType>\n'
        if p.get("apparel"):
            xml += f'    <Apparel>{xml_escape(p["apparel"])}</Apparel>\n'
        if p.get("goods_sub_type"):
            xml += f'    <GoodsSubType>{xml_escape(p["goods_sub_type"])}</GoodsSubType>\n'
        # Brand как отдельный элемент (НЕ в Option!)
        xml += f'    <Brand>{xml_escape(p["brand"])}</Brand>\n'
        # Size как отдельный элемент
        xml += f'    <Size>{xml_escape(p["size"])}</Size>\n'
        xml += f'    <Title>{xml_escape(p["title"])}</Title>\n'
        xml += f'    <Description>{xml_escape(p["description"])}</Description>\n'
        xml += f'    <Price>{p["price"]}</Price>\n'
        xml += f'    <Condition>{xml_escape(p["condition"])}</Condition>\n'
        xml += f'    <AdType>{xml_escape(p["ad_type"])}</AdType>\n'
        xml += f'    <Address>{xml_escape(p["address"])}</Address>\n'
        xml += f'    <City>Москва</City>\n'
        xml += f'    <ContactPhone>+79269006188</ContactPhone>\n'
        xml += f'    <ManagerName>Ле Буше</ManagerName>\n'

        if p.get("images"):
            xml += '    <Images>\n'
            for img in p["images"]:
                xml += f'      <Image url="{xml_escape(img)}"/>\n'
            xml += '    </Images>\n'

        xml += '  </Ad>\n'

    xml += '</Ads>\n'
    return xml


if __name__ == "__main__":
    xml = generate_xml()
    with open("avito.xml", "w", encoding="utf-8") as f:
        f.write(xml)
    print(f"✅ Сгенерирован avito.xml ({len(PRODUCTS)} товаров, {len(xml)} байт)")
    print()
    print("📋 Категории в фиде:")
    for p in PRODUCTS:
        cat = p.get("apparel_type") or p.get("apparel") or p.get("goods_sub_type")
        print(f"   {p['sku']} | Brand={p['brand']:14} Size={p['size']:10} | {cat}")
