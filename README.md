# SProvider

> Автономная поставщик расписания занятий.
> Входит в семейство проектов SPlatform.

 <!-- some shields -->
<p align="center">
  <a href='https://sparser.readthedocs.io/ru/latest/?badge=latest'>
    <img alt="Documentation", src='https://readthedocs.org/projects/sparser/badge/?version=latest'>
  </a>
  <img alt="Version" src="https://img.shields.io/badge/dynamic/toml?url=https%3A%2F%2Fcodeberg.org%2FSalormoon%2Fsparser%2Fraw%2Fbranch%2Fmain%2Fpyproject.toml&query=tool.poetry.version&prefix=v&label=version&color=green">
  <img alt="license" src="https://img.shields.io/badge/dynamic/toml?url=https%3A%2F%2Fcodeberg.org%2FSalormoon%2Fsparser%2Fraw%2Fbranch%2Fmain%2Fpyproject.toml&query=tool.poetry.license&label=license&color=red">
  <img alt="python" src="https://img.shields.io/badge/dynamic/toml?url=https%3A%2F%2Fcodeberg.org%2FSalormoon%2Fsparser%2Fraw%2Fbranch%2Fmain%2Fpyproject.toml&query=tool.poetry.dependencies.python&label=python&color=blue">
</p>

## Установка

Копируем репозиторий с проектом:

```bash
git clone https://github.com/pentergust/sprovider
cd sprovider
```

Устанавливаем зависимости через [uv](https://astral.sh/uv):

```bash
uv sync
```

## Запуск сервера

Перед первым запуском скопируйте файл `.env.dist` в `.env`.
В файле `.env` укажите необходимые настройки.

Через _Uv_:

```bash
uv run -m uvicorn provider.app:app
```

## Поддержка

Мы будем очень рады, если вы поддержите проект звёздочками.
Вы можете свободно предлагать свои идеи и правки.

Также стоит отметить что проект распространяется под свободной лицензией.
Это значит что вы можете брать и использовать код в своих целях.
Мы также предоставляем документацию, чтобы вам было удобнее разбираться
во всех компонентах.

Мы будем очень рады, если вы оставите свой вклад.
