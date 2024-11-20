import aiohttp

YANDEX_API_KEY = "a58dc7d1-3ddd-4550-9518-26a608032498"


async def get_location_address(latitude, longitude):
    API_URL = "https://geocode-maps.yandex.ru/1.x/"
    params = {
        "apikey": YANDEX_API_KEY,
        "geocode": f"{longitude},{latitude}",
        "format": "json"
    }

    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(API_URL, params=params) as response:
                if response.status == 200:
                    data = await response.json()
                    feature_member = data.get("response", {}).get("GeoObjectCollection", {}).get("featureMember", [])
                    if feature_member:
                        for geo_object in feature_member:
                            address = geo_object["GeoObject"]["metaDataProperty"]["GeocoderMetaData"]["Address"]
                            components = address.get("Components", [])

                            country = None
                            city = None
                            district = None
                            kvartal = None
                            for component in components:
                                if component["kind"] == "country":
                                    country = component["name"]
                                if component["kind"] == "locality":
                                    city = component["name"]
                                if component["kind"] == "district" and "район" in component["name"]:
                                    district = component["name"]
                                if component["kind"] == "district" and "квартал" in component["name"]:
                                    kvartal = component["name"]

                            result = []
                            if country:
                                result.append(country)
                            if city:
                                result.append(city)
                            if district:
                                result.append(district)
                            if kvartal:
                                result.append(kvartal)

                            return ", ".join(result) if result else "Manzil topilmadi."

                    return "Manzil topilmadi."
                else:
                    return f"API javobida xatolik: {response.status}"
        except Exception as e:
            return f"Xatolik: {str(e)}"
