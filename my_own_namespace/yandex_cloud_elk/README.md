# my_own_namespace.yandex_cloud_elk

Эта коллекция содержит собственный Ansible модуль и роль, которые были созданы в рамках домашнего задания по курсу Ansible.

## Модуль `my_own_file`

Модуль `my_own_namespace.yandex_cloud_elk.my_own_file` создаёт или обновляет текстовый файл на удалённом хосте по заданному пути с указанным содержимым.

### Параметры

- `path` (строка, обязательный) — путь к файлу, включая имя.
- `content` (строка, обязательный) — содержимое файла.
- `backup` (bool, опционально, по умолчанию `false`) — создать резервную копию файла, если он уже существует.

### Пример использования

```yaml
- name: Create file
  my_own_namespace.yandex_cloud_elk.my_own_file:
    path: /tmp/my_file.txt
    content: hello world
    backup: yes
```

 ## Скриншот шага №4
![скриншот](https://github.com/YuriKopshev/vector-role/blob/main/img/molecule_create.png);


 ## Скриншот шага №6
![скриншот](https://github.com/YuriKopshev/vector-role/blob/main/img/molecule_create.png);


 ## Скриншот шага №15
![скриншот](https://github.com/YuriKopshev/vector-role/blob/main/img/molecule_create.png);


 ## Скриншот шага №16
![скриншот](https://github.com/YuriKopshev/vector-role/blob/main/img/molecule_create.png);




