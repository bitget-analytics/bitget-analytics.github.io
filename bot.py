import os
import json
import random
import requests
from datetime import datetime

GH_TOKEN = os.getenv("GH_TOKEN")
REPO = "bitget-analytics/bitget-analytics.github.io"
REF_LINK = "https://partner.bitget.com/bg/vwmk5g3k"

def get_market_data():
    try:
        symbol = random.choice(["BTCUSDT", "ETHUSDT", "SOLUSDT"])
        oi_res = requests.get(f"https://fapi.binance.com/fapi/v1/openInterest?symbol={symbol}").json()
        funding_res = requests.get(f"https://fapi.binance.com/fapi/v1/premiumIndex?symbol={symbol}").json()
        
        oi = float(oi_res.get("openInterest", 0)) / 1_000_000
        funding = float(funding_res.get("lastFundingRate", 0)) * 100
        
        return {"symbol": symbol.replace("USDT", ""), "oi_mln": round(oi, 2), "funding_pct": round(funding, 4)}
    except:
        return {"symbol": "BTC", "oi_mln": 854.15, "funding_pct": 0.0115}

def generate_content():
    date_str = datetime.now().strftime("%Y-%m-%d %H:%M")
    data = get_market_data()
    
    ref_ru = f"<br><br><strong>Где реализовать этот сетап?</strong> Используйте профессиональные AI-инструменты, минимальные комиссии и торгуйте с гарантированной безопасностью резервов на бирже Bitget. <a href='{REF_LINK}' target='_blank' style='color:#00b4c9;text-decoration:underline;'>Зарегистрируйтесь сейчас и заберите Welcome Pack до 6,200 USDT</a>."
    ref_en = f"<br><br><strong>Where to trade this setup?</strong> Capitalize on lowest fees, advanced AI-automation, and 100% proven proof of reserves on Bitget. <a href='{REF_LINK}' target='_blank' style='color:#00b4c9;text-decoration:underline;'>Register via our link to claim your Welcome Pack up to 6,200 USDT</a>."
    ref_es = f"<br><br><strong>¿Dónde operar este setup?</strong> Aproveche las comisiones más bajas, herramientas de IA avanzadas y una Prueba de Reservas del 100% en Bitget. <a href='{REF_LINK}' target='_blank' style='color:#00b4c9;text-decoration:underline;'>Regístrese aquí y reclame su Welcome Pack de hasta 6,200 USDT</a>."

    if random.randint(1, 100) <= 80:
        direction_ru = "Лонг Сквиз (вынос покупателей)" if data["funding_pct"] > 0.01 else "Шорт Сквиз (топливо для роста)"
        direction_en = "Long Squeeze risk" if data["funding_pct"] > 0.01 else "Short Squeeze potential"
        direction_es = "riesgo de Long Squeeze" if data["funding_pct"] > 0.01 else "potencial de Short Squeeze"

        return {
            "date": date_str,
            "ru": {
                "badge": f"Сетап #{data['symbol']}",
                "title": f"Мониторинг деривативов {data['symbol']}: Дисбаланс позиций",
                "description": f"Текущий открытый интерес по активу составляет {data['oi_mln']} млн. Ставка финансирования флэт-позиций фиксируется на уровне {data['funding_pct']}%. Визуальный перекос в стакане фьючерсов указывает на высокую вероятность сценария: {direction_ru}. Пока толпа лудоманов загружает маркет-ордера с огромными плечами в надежде обыграть математику, крупные игроки аккумулируют ликвидность для направленного выноса. Рекомендуется убрать эмоции, рассчитать риск-менеджмент и подтянуть стоп-ордера.{ref_ru}"
            },
            "en": {
                "badge": f"Setup #{data['symbol']}",
                "title": f"{data['symbol']} Technical Analysis: Orderbook Imbalance",
                "description": f"Open Interest stands firmly at {data['oi_mln']}M with the current funding rate holding at {data['funding_pct']}%. Derivative data analysis signals a clear {direction_en}. Retail leverage is severely overextended across major exchanges. While amateur traders treat this market like a casino, smart money is preparing for a liquidity sweep. Adjust your protective stops immediately.{ref_en}"
            },
            "es": {
                "badge": f"Análisis #{data['symbol']}",
                "title": f"Desequilibrio de Derivados en {data['symbol']}",
                "description": f"El Interés Abierto se sitúa en {data['oi_mln']}M con una tasa de financiación ponderada de {data['funding_pct']}%. Los flujos de órdenes reflejan un {direction_es}. Los operadores minoristas continúan apalancando posiciones al límite, ignorando la mecánica del mercado. Mantenga una estrategia estricta de gestión de riesgos.{ref_es}"
            }
        }
    else:
        topics = [
            {
                "ru": {"badge": "Аналитика", "title": "Проклятие крипто-лудомана: почему математика всегда побеждает", "desc": f"В индустрии цифровых активов быстро привыкаешь списывать потери на высокую волатильность, манипуляции маркетмейкеров или откровенный скам проектов. Но жесткая реальность заключается в том, что 100% лудоманов прокляты и будут лишены своего капитала просто по законам математики. Ваша торговля заканчивается в тот самый момент, когда вы путаете системный расчет математического ожидания с игрой на тотализаторе. Единственный способ выжить на дистанции — убрать эмоции и использовать надежные торговые экосистемы.{ref_ru}"},
                "en": {"badge": "Market Psychology", "title": "The Retail Illusion: Why 100% of Gamblers Blow Their Accounts", "desc": f"In crypto, uneducated traders love to blame volatility, whales, or bad luck for their catastrophic failures. The cold truth is that capital destruction is guaranteed by pure mathematics the exact second you mistake a professional leveraged ecosystem for a casino slot machine. To survive the long game, you must eliminate emotional bias and build strict rules.{ref_en}"},
                "es": {"badge": "Psicología", "title": "La ilusión del trading minorista: por qué la matemática nunca falla", "desc": f"Es común culpar a la manipulación del mercado cuando una cuenta queda en cero. Sin embargo, la realidad financiera es implacable: la pérdida de capital está garantizada cuando se confunde el análisis de datos con apuestas emocionales. La única forma de mantener consistencia es operar sin sesgos y con herramientas profesionales.{ref_es}"}
            },
            {
                "ru": {"badge": "Безопасность", "title": "Кибербезопасность смартфона как фундамент вашего депозита", "desc": f"Трейдеры могут часами изучать графики, искать аномальный открытый интерес и анализировать отчеты CME, полностью забывая о базовой гигиене устройств. Но если ваша приватность нарушена на уровне операционной системы смартфона — безопасность ваших ключей и кошельков равна нулю. Там, где заканчивается контроль над собственными данными, очень быстро заканчиваются и деньги. Торгуйте только на защищенных платформах мирового уровня.{ref_ru}"},
                "en": {"badge": "Security Guide", "title": "Device Privacy: The Unseen Foundation of Your Trading Account", "desc": f"Traders spend days mastering order flow analytics and chart patterns while completely ignoring fundamental device security. If your smartphone leaks data, your cold storage and account safety are a complete illusion. Where digital privacy ends, financial loss inevitably follows. Ensure your capital is managed on a top-tier secure exchange.{ref_en}"},
                "es": {"badge": "Seguridad", "title": "La seguridad del dispositivo: el pilar invisible de sus fondos", "desc": f"Muchos analizan patrones gráficos durante horas pero olvidan la seguridad digital básica. Si el sistema operativo de su teléfono está comprometido, la protección de sus contraseñas es inexistente. Donde
