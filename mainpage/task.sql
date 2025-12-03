CREATE TABLE Task( 
    id            serial primary key, 
    dt            timestamp null,
    deadline      timestamp not null, 
    `description` varchar(1024), 
    executor      int references user(id),
    done          boolean
);
-- Не надо выполнять этот запрос в БД!
-- Это пример запроса, который выполняется в консоли,
-- и теперь за нас его выполнит Django