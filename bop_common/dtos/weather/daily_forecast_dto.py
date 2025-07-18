from dataclasses import dataclass

@dataclass
class DailyForecastDTO:
    date: str
    temperature: float
    description: str