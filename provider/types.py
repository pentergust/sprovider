"""Используемые типы в поставщике расписания."""

from collections.abc import Mapping, MutableSequence, Sequence
from datetime import datetime, time
from typing import Literal

from pydantic import BaseModel


class ProviderStatus(BaseModel):
    """Техническая информация о поставщике.
    
    Может быть использована чтобы отличать несколько поставщиков.
    """

    name: str
    version: str
    url: str

class ScheduleStatus(BaseModel):
    """Информация о расписании.
    
    Они же метаданные о расписании.
    Расписывают откуда было загружено расписание.
    Используется для проверки актуальности расписания.
    """

    source: str
    """Имя источника расписания. Гугл таблицы, файл, сайт или другое."""

    url: str
    """Ссылка на источник. Название файла или прочее."""

    hash: str
    """Уникальный хеш расписания.
    
    Используется при быстрой проверке обновлений.
    """

    check_at: datetime
    """Время последней проверки изменений в расписании."""

    update_at: datetime
    """Время последнего обновления расписания."""

    next_check: datetime
    """Когда будет произведена следующая проверка изменений."""


class ScheduleMeta(BaseModel):
    """Необходимые метаданные для расписания.
    
    Минимальный набор параметров, который загружается при запуске.
    Обязательно стоит указать название и источник расписание.
    Остальные параметры заполняются автоматически поставщиком.
    """

    source: str
    url: str
    hash: str | None = None
    check_at: datetime | None = None
    update_at: datetime | None = None
    next_check: datetime | None = None


class Status(BaseModel):
    """Информация поставщике.
    
    Технические подробности поставщика.
    Можно использовать если в проекте используется несколько поставщиков.
    
    Предоставляет информацию о расписании.
    Используется для автоматической проверка обновлений.
    """

    provider: ProviderStatus
    schedule: ScheduleStatus

class LessonTime(BaseModel):
    """Время урока для расписания звонков."""

    start: time
    end: time

TimeTable = Sequence[LessonTime]

class Lesson(BaseModel):
    """Урок в расписании."""

    name: str | None
    """Имя предмета. Может быть пустым, если занятие отменено."""

    cabinets: list[str]
    """В каких кабинетах проводится занятие.
    
    Может быть несколько кабинетов, если класс делится на группы.
    """

# Дополнительные типы для расписания
DayLessons = MutableSequence[Lesson | None]
ClassLessons = Sequence[DayLessons]
ScheduleT = Mapping[str, ClassLessons]

class Schedule(BaseModel):
    """Полное расписание уроков."""

    schedule: ScheduleT

Day = Literal[0, 1, 2, 3, 4, 5]

class ScheduleFilter(BaseModel):
    """Фильтры для получения расписания.
    
    Передаются при получении расписания.
    Можно не передавать, тогда будет получено полное расписание.
    """

    days: Sequence[Day] | None = None
    """Для каких дней недели.
    
    Если не передавать, отдаст расписание не всю неделю.
    """

    cl: Sequence[str] | None = None
    """Для каких классов.
    
    Если не передавать, отдаст расписание для всех классов.
    """
