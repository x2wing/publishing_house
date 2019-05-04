publishing_company
CREATE TABLE CLASS(
    CLASS_ID bigserial PRIMARY KEY,
    CLASS_NAME text);
    
CREATE TABLE BOOK (
    BOOK_IDENTIFIER bigserial PRIMARY KEY,
    NAME_OF_BOOK text, --название книги
    AUTHOR_OF_BOOK text, --автор
    QUANTITY_OF_PAGES integer, -- число страниц
    QUANTITY_OF_COPYES bigint, -- число копий 
    PRICE_OF_BOOK money); -- цена книги
    
CREATE TABLE CLIENTS(
    CLIENT_ID bigserial PRIMARY KEY,
    CLIENT_NAME text, -- имя клиента
    CLIENT_LAST_NAME text, -- фамилия
    CLIENT_MIDDLE_NAME text, -- отчество
    CLIENT_PHONE_NUMBER text); -- номер телефона
    
CREATE TABLE  SHOPS(
    SHOP_ID bigserial PRIMARY KEY,
    SHOP_NAME text, -- название магазина
    SHOP_ADDRESS text); -- адресс магазина
    
CREATE TABLE PROVIDER(
    PROVIDER_ID bigserial PRIMARY KEY,
    PROVIDER_ORGANIZATION text, -- название поставщика
    PROVIDER_ADDRESS text, -- адрес поставщика
    PROVIDER_PHONE_NUMBER text); -- телефон поставщика
    
CREATE TABLE WORKER_INFO(
    WORKER_ID bigserial PRIMARY KEY,
    WORKER_LAST_NAME text, -- фамилия
    WORKER_NAME text, -- имя
    WORKER_MIDDLE_NAME text, -- отчество
    WORKER_PASSPORT_SERIES text, -- серия паспорта
    WORKER_PASSPORT_ID text, -- номер паспорта
    WORKER_POSITION_HELD text, -- название должности
    WORKER_PLACE_OF_RESIDENT text); -- регистрация

CREATE TABLE SALARY (
    WORKER_ID bigint UNIQUE references WORKER_INFO(WORKER_ID),
    WORKER_SALARY money, -- зарплата 
    WORKER_PREMIUM money, -- премия
    WORKER_PREPAID_EXPENSE money); -- аванс



CREATE TABLE ORDER_OF_BOOKS (
    ORDER_ID bigserial PRIMARY KEY,
    PROVIDER_ID bigint REFERENCES PROVIDER(PROVIDER_ID) ON DELETE CASCADE ON UPDATE CASCADE,
    SHOP_ID bigint REFERENCES SHOPS(SHOP_ID) ON DELETE CASCADE ON UPDATE CASCADE,
    CLIENT_ID bigint REFERENCES CLIENTS(CLIENT_ID) ON DELETE CASCADE ON UPDATE CASCADE,
    DATE_OF_ORDER timestamp DEFAULT current_timestamp,
    SUMM_OF_PREPAYMENT money,
    DATE_OF_COMPLETION timestamp,
    WORKER_ID bigint REFERENCES WORKER_INFO(WORKER_ID) ON DELETE CASCADE ON UPDATE CASCADE, -- куратор заказа
    IS_ACTIVE boolean,
    CLASS_ID bigint REFERENCES CLASS(CLASS_ID) ON DELETE CASCADE ON UPDATE CASCADE); 

CREATE TABLE PRODUCTION (
    ORDER_ID bigint REFERENCES ORDER_OF_BOOKS(ORDER_ID) ON DELETE CASCADE ON UPDATE CASCADE,
    BOOK_IDENTIFIER integer REFERENCES BOOK(BOOK_IDENTIFIER) ON DELETE CASCADE ON UPDATE CASCADE);

CREATE TABLE SUPPLY (
    PROVIDER_ID bigint REFERENCES PROVIDER(PROVIDER_ID) ON DELETE CASCADE ON UPDATE CASCADE,
    SUPPLY_DATE_AND_TIME timestamp);





uniquie references t1(kod)

CREATE OR REPLACE FUNCTION get_next_version()
    RETURNS bigint AS
   $BODY$
    INSERT INTO versions (nversion) (SELECT COALESCE((SELECT max(nversion) + 1 FROM versions), 1)) 
    RETURNING version_id;
   $BODY$
 LANGUAGE 'sql' VOLATILE;

        
                INSERT INTO main.projects (project_name) VALUES ('%(project)s');