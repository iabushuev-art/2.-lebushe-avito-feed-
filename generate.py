"""
Avito Autoload Feed Generator for Le Bushe.
Генерирует XML-фид в формате Avito Autoload v4 из каталога товаров.

Использование:
    python3 generate.py
    
Результат: avito.xml в текущей директории.
"""
import json
from xml.sax.saxutils import escape

# Категории Avito
CATEGORIES = {
    "рубашка_мужская": "27_27_25",
    "кроссовки": "27_27_16_18",
    "туфли": "27_27_16_4",
    "толстовка": "27_27_17_19",
    "по_умолчанию": "27",
}

BRAND_MAP = {
    "BURBERRY": "Берберри",
    "OLYMP": "Olymp",
    "GUESS": "Guess",
    "PLEIN SPORT": "Plein Sport",
}

PRODUCTS = [
    {
        "sku": "52056",
        "title": "Рубашка мужская OLYMP LUXOR modern fit, р.L (large), хлопок 100%, отличное",
        "description": "Рубашка мужская OLYMP LUXOR modern fit, размер L (large). Классическая мужская рубашка от премиального немецкого бренда OLYMP. Силуэт modern fit — современная посадка между slim и regular. Цвет — голубой с мелкой повторяющейся клеткой (микро-узор из тёмно-синих и белых элементов). Контрастная отделка внутренней стороны воротника и манжет — однотонный голубой. Пуговицы белые. Нагрудный карман слева. Состав: 100% хлопок (Baumwolle/Cotton). Уход: машинная стирка при 40°. Код производителя: 1258|69|11. Артикул галереи: 52056. Состояние: б/у, в отличном виде — практически как новая. Без следов носки, потёртостей, пятен и других дефектов.",
        "category": "рубашка_мужская",
        "price": 1990,
        "brand": "OLYMP",
        "condition": "б/у",
        "size": "L",
        "color": "голубой",
        "material": "хлопок",
        "address": "Москва, пр-т Маршала Жукова, 39к1",
        "images": [
            "https://avatars.mds.yandex.net/get-yastore/21580234/9vm2cphzkrgmnjsslfkkvwt6x8mbn8xf/orig",
            "https://avatars.mds.yandex.net/get-yastore/20493671/ztx4dwk4vhd8rt84p6rfsbvtmdp9p6l9/orig",
        ],
    },
    {
        "sku": "00575",
        "title": "Кроссовки Plein Sport Lo-Top, р.43, белый/чёрный, новые с биркой",
        "description": "Кроссовки мужские Plein Sport Lo-Top Sneakers, размер 43. Спортивные кроссовки от итальянского бренда Plein Sport (суббренд Philipp Plein). Линейка Sport — активный молодёжный стиль, сочетание streetwear и люкса. Силуэт Lo-Top — низкие кроссовки с массивной подошвой. Верх — текстиль (mesh) с кожаными вставками и большим логотипом PS. Подошва — массивная белая платформа. Цвет — белый с чёрными акцентами. Артикул производителя: SADS USC0611 STE003N. Артикул галереи: 00575. Состояние: новые, с биркой. Производство: MADE IN CHINA.",
        "category": "кроссовки",
        "price": 7990,
        "brand": "PLEIN SPORT",
        "condition": "новое",
        "size": "43",
        "color": "белый",
        "material": "текстиль",
        "address": "Москва, пр-т Маршала Жукова, 39к1",
        "images": [
            "https://avatars.mds.yandex.net/get-yastore/21580234/9vm2cphzkrgmnjsslfkkvwt6x8mbn8xf/orig",
        ],
    },
    {
        "sku": "00576",
        "title": "Туфли женские Guess ESSENTIALS, р.36, монограммный принт, новые с биркой",
        "description": "Туфли женские Guess ESSENTIALS, размер 36. Классические женские лодочки на каблуке от американского бренда Guess. Коллекция ESSENTIALS — базовая линейка бренда, фирменный паттерн 4G в монохромном исполнении. Силуэт — классические pointed-toe pumps на высокой шпильке. Верх — текстиль с фирменным монограммным узором Guess 4G. Каблук — высокая шпилька. Подкладка и стелька — натуральная кожа, логотип Guess на стельке. Размер EUR 36. Артикул галереи: 00576. Состояние: новые, с биркой.",
        "category": "туфли",
        "price": 2990,
        "brand": "GUESS",
        "condition": "новое",
        "size": "36",
        "color": "черно-белый",
        "material": "текстиль",
        "address": "Москва, пр-т Маршала Жукова, 39к1",
        "images": [
            "https://avatars.mds.yandex.net/get-yastore/21580234/9vm2cphzkrgmnjsslfkkvwt6x8mbn8xf/orig",
        ],
    },
    {
        "sku": "00579",
        "title": "Кеды Guess Sock Sneakers, р.39, чёрные с золотой лентой, отличное",
        "description": "Кеды (слипоны) женские Guess Sock Sneakers, размер 39. Женские высокие слипоны в стиле sport-chic от Guess. Силуэт — sock-style, высокий чулок из эластичного текстиля, надевается без шнурков. Верх — чёрный текстиль (стрейч), облегает щиколотку. Горловина отделана фирменной золотистой лентой с повторяющимся логотипом GUESS. Подошва — массивная белая платформа с резиновым рантом, GUESS тиснён на подошве. Размер EUR 39. Артикул галереи: 00579. Состояние: б/у, в отличном виде. Сезон: демисезон.",
        "category": "кроссовки",
        "price": 3990,
        "brand": "GUESS",
        "condition": "б/у",
        "size": "39",
        "color": "черный",
        "material": "текстиль",
        "address": "Москва, пр-т Маршала Жукова, 39к1",
        "images": [
            "https://avatars.mds.yandex.net/get-yastore/21580234/9vm2cphzkrgmnjsslfkkvwt6x8mbn8xf/orig",
        ],
    },
    {
        "sku": "27349",
        "title": "Толстовка Burberry Knightsbridge Octopus, унисекс, р.L, модал 100%, отличное",
        "description": "Толстовка (худи) Burberry Knightsbridge Octopus Print, размер L, унисекс. Лимитированная толстовка от Burberry из линейки Knightsbridge — капсульная коллекция к юбилею лондонского адреса Horseferry House SW1. Силуэт — классический худи с капюшоном на шнурках, кенгуру-карман, длинный рукав. Принт — крупная графика осьминога (коричнево-оранжевые щупальца с присосками). Факсимильный лейбл Burberry, Knightsbridge SW1, Kingdom, LONDON ENGLAND. Состав: 100% модал. Производство: Италия. Замеры (см): плечи 50, грудь 62, спинка 72, рукав от плеча 70, рукав от подмышки 53. Артикул галереи: 27349. Состояние: б/у, в отличном виде. Стиль: спорт-стрит.",
        "category": "толстовка",
        "price": 18490,
        "brand": "BURBERRY",
        "condition": "б/у",
        "size": "L",
        "color": "черный",
        "material": "модал",
        "address": "Москва, пр-т Маршала Жукова, 39к1",
        "images": [
            "https://avatars.mds.yandex.net/get-yastore/21580234/9vm2cphzkrgmnjsslfkkvwt6x8mbn8xf/orig",
        ],
    },
]


def generate_xml():
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml += '<Ads target="Avito.ru" formatVersion="3">\n'
    
    for p in PRODUCTS:
        xml += f'  <Ad>\n'
        xml += f'    <Id>{escape(p["sku"])}</Id>\n'
        xml += f'    <Title>{escape(p["title"])}</Title>\n'
        xml += f'    <Description>{escape(p["description"])}</Description>\n'
        xml += f'    <Price>{p["price"]}</Price>\n'
        xml += f'    <Category>{CATEGORIES.get(p["category"], CATEGORIES["по_умолчанию"])}</Category>\n'
        xml += f'    <Condition>{escape(p["condition"])}</Condition>\n'
        xml += f'    <City>Москва</City>\n'
        xml += f'    <Address>{escape(p["address"])}</Address>\n'
        xml += f'    <ContactPhone>+79269006188</ContactPhone>\n'
        if p.get("images"):
            xml += '    <Images>\n'
            for img in p["images"]:
                xml += f'      <Image url="{escape(img)}"/>\n'
            xml += '    </Images>\n'
        xml += '    <CustomOptions>\n'
        xml += f'      <Option name="Бренд">{escape(BRAND_MAP.get(p["brand"], p["brand"]))}</Option>\n'
        xml += f'      <Option name="Размер">{escape(p["size"])}</Option>\n'
        xml += f'      <Option name="Цвет">{escape(p["color"])}</Option>\n'
        xml += f'      <Option name="Материал">{escape(p["material"])}</Option>\n'
        xml += '      <Option name="Вид объявления">Продаю своё</Option>\n'
        xml += '      <Option name="Способ связи">Сообщения</Option>\n'
        xml += '    </CustomOptions>\n'
        xml += f'  </Ad>\n'
    
    xml += '</Ads>\n'
    return xml


if __name__ == "__main__":
    xml = generate_xml()
    with open("avito.xml", "w", encoding="utf-8") as f:
        f.write(xml)
    print(f"✅ Сгенерирован avito.xml ({len(PRODUCTS)} товаров)")
