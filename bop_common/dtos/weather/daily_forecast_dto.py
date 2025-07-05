from dataclasses import dataclass

@dataclass
class DailyForecastDTO:
    date: str
    temperature: int
    description: str