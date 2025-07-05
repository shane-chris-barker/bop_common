from bop_common.dtos.weather.weather_data_dto import WeatherDataDTO
from bop_common.dtos.weather.daily_forecast_dto import DailyForecastDTO

class TestWeatherDataDTO:

    def test_to_dict(self):
        daily_dtos = [
            DailyForecastDTO(
                date='03-07-2025',
                temperature=28,
                description='A sunny day'
            ),
            DailyForecastDTO(
                date='04-07-2025',
                temperature=7,
                description='A cold day'
            ),
        ]

        dto = WeatherDataDTO(
            city='Nottingham',
            forecast=daily_dtos
        )

        result = dto.to_dict()
        assert result == {
            'city': 'Nottingham',
            'forecast': [
                {'date': '03-07-2025', 'description': 'A sunny day', 'temperature': 28},
                {'date': '04-07-2025', 'description': 'A cold day', 'temperature': 7}
            ]
        }

    def test_from_dict(self):
        data = {
            'city': 'Nottingham',
            'forecast': [
                {'date': '03-07-2025', 'description': 'A sunny day', 'temperature': 28},
                {'date': '04-07-2025', 'description': 'A cold day', 'temperature': 7}
            ]
        }

        dto = WeatherDataDTO.from_dict(data)
        assert isinstance(dto, WeatherDataDTO)
        assert dto.city == 'Nottingham'
        assert isinstance(dto.forecast[0], DailyForecastDTO)
        assert dto.forecast[0].date == '03-07-2025'
        assert dto.forecast[0].temperature == 28
        assert dto.forecast[0].description == 'A sunny day'

        assert dto.forecast[1].date == '04-07-2025'
        assert dto.forecast[1].temperature == 7
        assert dto.forecast[1].description == 'A cold day'



