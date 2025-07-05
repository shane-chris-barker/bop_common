from dataclasses import dataclass
from typing import List, Dict
from bop_common.dtos.weather.daily_forecast_dto import DailyForecastDTO


@dataclass
class WeatherDataDTO:
    city: str
    forecast: List[DailyForecastDTO]

    def to_dict(self) -> Dict:
        return {
            "city": self.city,
            "forecast": [f.__dict__ for f in self.forecast]
        }

    @staticmethod
    def from_dict(data: Dict) -> "WeatherDataDTO":
        return WeatherDataDTO(
            city=data["city"],
            forecast=[DailyForecastDTO(**f) for f in data["forecast"]]
        )

