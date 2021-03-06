PGDMP     	    /                w            publishing_company    11.1    11.1 E    `           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                       false            a           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                       false            b           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                       false            c           1262    33250    publishing_company    DATABASE     �   CREATE DATABASE publishing_company WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'Russian_Russia.1251' LC_CTYPE = 'Russian_Russia.1251';
 "   DROP DATABASE publishing_company;
             postgres    false            �            1259    33927    book    TABLE     �   CREATE TABLE public.book (
    book_identifier bigint NOT NULL,
    name_of_book text,
    author_of_book text,
    quantity_of_pages integer,
    quantity_of_copyes bigint,
    price_of_book money
);
    DROP TABLE public.book;
       public         postgres    false            �            1259    33925    book_book_identifier_seq    SEQUENCE     �   CREATE SEQUENCE public.book_book_identifier_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 /   DROP SEQUENCE public.book_book_identifier_seq;
       public       postgres    false    199            d           0    0    book_book_identifier_seq    SEQUENCE OWNED BY     U   ALTER SEQUENCE public.book_book_identifier_seq OWNED BY public.book.book_identifier;
            public       postgres    false    198            �            1259    33916    class    TABLE     L   CREATE TABLE public.class (
    class_id bigint NOT NULL,
    class text
);
    DROP TABLE public.class;
       public         postgres    false            �            1259    33914    class_class_id_seq    SEQUENCE     {   CREATE SEQUENCE public.class_class_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 )   DROP SEQUENCE public.class_class_id_seq;
       public       postgres    false    197            e           0    0    class_class_id_seq    SEQUENCE OWNED BY     I   ALTER SEQUENCE public.class_class_id_seq OWNED BY public.class.class_id;
            public       postgres    false    196            �            1259    33938    clients    TABLE     �   CREATE TABLE public.clients (
    client_id bigint NOT NULL,
    client_name text,
    client_last_name text,
    client_middle_name text,
    client_phone_number text
);
    DROP TABLE public.clients;
       public         postgres    false            �            1259    33936    clients_client_id_seq    SEQUENCE     ~   CREATE SEQUENCE public.clients_client_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 ,   DROP SEQUENCE public.clients_client_id_seq;
       public       postgres    false    201            f           0    0    clients_client_id_seq    SEQUENCE OWNED BY     O   ALTER SEQUENCE public.clients_client_id_seq OWNED BY public.clients.client_id;
            public       postgres    false    200            �            1259    33992    order_of_books    TABLE     d  CREATE TABLE public.order_of_books (
    order_id bigint NOT NULL,
    provider_id bigint,
    shop_id bigint,
    client_id bigint,
    date_of_order timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    summ_of_prepayment money,
    date_of_completion timestamp without time zone,
    worker_id bigint,
    is_active boolean,
    class_id bigint
);
 "   DROP TABLE public.order_of_books;
       public         postgres    false            �            1259    33990    order_of_books_order_id_seq    SEQUENCE     �   CREATE SEQUENCE public.order_of_books_order_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 2   DROP SEQUENCE public.order_of_books_order_id_seq;
       public       postgres    false    210            g           0    0    order_of_books_order_id_seq    SEQUENCE OWNED BY     [   ALTER SEQUENCE public.order_of_books_order_id_seq OWNED BY public.order_of_books.order_id;
            public       postgres    false    209            �            1259    34024 
   production    TABLE     k   CREATE TABLE public.production (
    order_id bigint,
    book_identifier integer,
    quantity integer
);
    DROP TABLE public.production;
       public         postgres    false            �            1259    33960    provider    TABLE     �   CREATE TABLE public.provider (
    provider_id bigint NOT NULL,
    provider_organization text,
    provider_address text,
    provider_phone_number text
);
    DROP TABLE public.provider;
       public         postgres    false            �            1259    33958    provider_provider_id_seq    SEQUENCE     �   CREATE SEQUENCE public.provider_provider_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 /   DROP SEQUENCE public.provider_provider_id_seq;
       public       postgres    false    205            h           0    0    provider_provider_id_seq    SEQUENCE OWNED BY     U   ALTER SEQUENCE public.provider_provider_id_seq OWNED BY public.provider.provider_id;
            public       postgres    false    204            �            1259    33980    salary    TABLE     �   CREATE TABLE public.salary (
    worker_id bigint,
    worker_salary money,
    worker_premium money,
    worker_prepaid_expense money
);
    DROP TABLE public.salary;
       public         postgres    false            �            1259    33949    shops    TABLE     f   CREATE TABLE public.shops (
    shop_id bigint NOT NULL,
    shop_name text,
    shop_address text
);
    DROP TABLE public.shops;
       public         postgres    false            �            1259    33947    shops_shop_id_seq    SEQUENCE     z   CREATE SEQUENCE public.shops_shop_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 (   DROP SEQUENCE public.shops_shop_id_seq;
       public       postgres    false    203            i           0    0    shops_shop_id_seq    SEQUENCE OWNED BY     G   ALTER SEQUENCE public.shops_shop_id_seq OWNED BY public.shops.shop_id;
            public       postgres    false    202            �            1259    34037    supply    TABLE     m   CREATE TABLE public.supply (
    provider_id bigint,
    supply_date_and_time timestamp without time zone
);
    DROP TABLE public.supply;
       public         postgres    false            �            1259    33971    worker_info    TABLE       CREATE TABLE public.worker_info (
    worker_id bigint NOT NULL,
    worker_last_name text,
    worker_name text,
    worker_middle_name text,
    worker_passport_series text,
    worker_passport_id text,
    worker_position_held text,
    worker_place_of_resident text
);
    DROP TABLE public.worker_info;
       public         postgres    false            �            1259    33969    worker_info_worker_id_seq    SEQUENCE     �   CREATE SEQUENCE public.worker_info_worker_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 0   DROP SEQUENCE public.worker_info_worker_id_seq;
       public       postgres    false    207            j           0    0    worker_info_worker_id_seq    SEQUENCE OWNED BY     W   ALTER SEQUENCE public.worker_info_worker_id_seq OWNED BY public.worker_info.worker_id;
            public       postgres    false    206            �
           2604    33930    book book_identifier    DEFAULT     |   ALTER TABLE ONLY public.book ALTER COLUMN book_identifier SET DEFAULT nextval('public.book_book_identifier_seq'::regclass);
 C   ALTER TABLE public.book ALTER COLUMN book_identifier DROP DEFAULT;
       public       postgres    false    198    199    199            �
           2604    33919    class class_id    DEFAULT     p   ALTER TABLE ONLY public.class ALTER COLUMN class_id SET DEFAULT nextval('public.class_class_id_seq'::regclass);
 =   ALTER TABLE public.class ALTER COLUMN class_id DROP DEFAULT;
       public       postgres    false    196    197    197            �
           2604    33941    clients client_id    DEFAULT     v   ALTER TABLE ONLY public.clients ALTER COLUMN client_id SET DEFAULT nextval('public.clients_client_id_seq'::regclass);
 @   ALTER TABLE public.clients ALTER COLUMN client_id DROP DEFAULT;
       public       postgres    false    201    200    201            �
           2604    33995    order_of_books order_id    DEFAULT     �   ALTER TABLE ONLY public.order_of_books ALTER COLUMN order_id SET DEFAULT nextval('public.order_of_books_order_id_seq'::regclass);
 F   ALTER TABLE public.order_of_books ALTER COLUMN order_id DROP DEFAULT;
       public       postgres    false    210    209    210            �
           2604    33963    provider provider_id    DEFAULT     |   ALTER TABLE ONLY public.provider ALTER COLUMN provider_id SET DEFAULT nextval('public.provider_provider_id_seq'::regclass);
 C   ALTER TABLE public.provider ALTER COLUMN provider_id DROP DEFAULT;
       public       postgres    false    205    204    205            �
           2604    33952    shops shop_id    DEFAULT     n   ALTER TABLE ONLY public.shops ALTER COLUMN shop_id SET DEFAULT nextval('public.shops_shop_id_seq'::regclass);
 <   ALTER TABLE public.shops ALTER COLUMN shop_id DROP DEFAULT;
       public       postgres    false    203    202    203            �
           2604    33974    worker_info worker_id    DEFAULT     ~   ALTER TABLE ONLY public.worker_info ALTER COLUMN worker_id SET DEFAULT nextval('public.worker_info_worker_id_seq'::regclass);
 D   ALTER TABLE public.worker_info ALTER COLUMN worker_id DROP DEFAULT;
       public       postgres    false    207    206    207            P          0    33927    book 
   TABLE DATA               �   COPY public.book (book_identifier, name_of_book, author_of_book, quantity_of_pages, quantity_of_copyes, price_of_book) FROM stdin;
    public       postgres    false    199   nQ       N          0    33916    class 
   TABLE DATA               0   COPY public.class (class_id, class) FROM stdin;
    public       postgres    false    197   jR       R          0    33938    clients 
   TABLE DATA               t   COPY public.clients (client_id, client_name, client_last_name, client_middle_name, client_phone_number) FROM stdin;
    public       postgres    false    201   �R       [          0    33992    order_of_books 
   TABLE DATA               �   COPY public.order_of_books (order_id, provider_id, shop_id, client_id, date_of_order, summ_of_prepayment, date_of_completion, worker_id, is_active, class_id) FROM stdin;
    public       postgres    false    210   /S       \          0    34024 
   production 
   TABLE DATA               I   COPY public.production (order_id, book_identifier, quantity) FROM stdin;
    public       postgres    false    211   LS       V          0    33960    provider 
   TABLE DATA               o   COPY public.provider (provider_id, provider_organization, provider_address, provider_phone_number) FROM stdin;
    public       postgres    false    205   iS       Y          0    33980    salary 
   TABLE DATA               b   COPY public.salary (worker_id, worker_salary, worker_premium, worker_prepaid_expense) FROM stdin;
    public       postgres    false    208   T       T          0    33949    shops 
   TABLE DATA               A   COPY public.shops (shop_id, shop_name, shop_address) FROM stdin;
    public       postgres    false    203   3T       ]          0    34037    supply 
   TABLE DATA               C   COPY public.supply (provider_id, supply_date_and_time) FROM stdin;
    public       postgres    false    212   PT       X          0    33971    worker_info 
   TABLE DATA               �   COPY public.worker_info (worker_id, worker_last_name, worker_name, worker_middle_name, worker_passport_series, worker_passport_id, worker_position_held, worker_place_of_resident) FROM stdin;
    public       postgres    false    207   �T       k           0    0    book_book_identifier_seq    SEQUENCE SET     F   SELECT pg_catalog.setval('public.book_book_identifier_seq', 5, true);
            public       postgres    false    198            l           0    0    class_class_id_seq    SEQUENCE SET     A   SELECT pg_catalog.setval('public.class_class_id_seq', 1, false);
            public       postgres    false    196            m           0    0    clients_client_id_seq    SEQUENCE SET     C   SELECT pg_catalog.setval('public.clients_client_id_seq', 3, true);
            public       postgres    false    200            n           0    0    order_of_books_order_id_seq    SEQUENCE SET     J   SELECT pg_catalog.setval('public.order_of_books_order_id_seq', 1, false);
            public       postgres    false    209            o           0    0    provider_provider_id_seq    SEQUENCE SET     F   SELECT pg_catalog.setval('public.provider_provider_id_seq', 3, true);
            public       postgres    false    204            p           0    0    shops_shop_id_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('public.shops_shop_id_seq', 1, false);
            public       postgres    false    202            q           0    0    worker_info_worker_id_seq    SEQUENCE SET     H   SELECT pg_catalog.setval('public.worker_info_worker_id_seq', 16, true);
            public       postgres    false    206            �
           2606    33935    book book_pkey 
   CONSTRAINT     Y   ALTER TABLE ONLY public.book
    ADD CONSTRAINT book_pkey PRIMARY KEY (book_identifier);
 8   ALTER TABLE ONLY public.book DROP CONSTRAINT book_pkey;
       public         postgres    false    199            �
           2606    33924    class class_pkey 
   CONSTRAINT     T   ALTER TABLE ONLY public.class
    ADD CONSTRAINT class_pkey PRIMARY KEY (class_id);
 :   ALTER TABLE ONLY public.class DROP CONSTRAINT class_pkey;
       public         postgres    false    197            �
           2606    33946    clients clients_pkey 
   CONSTRAINT     Y   ALTER TABLE ONLY public.clients
    ADD CONSTRAINT clients_pkey PRIMARY KEY (client_id);
 >   ALTER TABLE ONLY public.clients DROP CONSTRAINT clients_pkey;
       public         postgres    false    201            �
           2606    33998 "   order_of_books order_of_books_pkey 
   CONSTRAINT     f   ALTER TABLE ONLY public.order_of_books
    ADD CONSTRAINT order_of_books_pkey PRIMARY KEY (order_id);
 L   ALTER TABLE ONLY public.order_of_books DROP CONSTRAINT order_of_books_pkey;
       public         postgres    false    210            �
           2606    33968    provider provider_pkey 
   CONSTRAINT     ]   ALTER TABLE ONLY public.provider
    ADD CONSTRAINT provider_pkey PRIMARY KEY (provider_id);
 @   ALTER TABLE ONLY public.provider DROP CONSTRAINT provider_pkey;
       public         postgres    false    205            �
           2606    33984    salary salary_worker_id_key 
   CONSTRAINT     [   ALTER TABLE ONLY public.salary
    ADD CONSTRAINT salary_worker_id_key UNIQUE (worker_id);
 E   ALTER TABLE ONLY public.salary DROP CONSTRAINT salary_worker_id_key;
       public         postgres    false    208            �
           2606    33957    shops shops_pkey 
   CONSTRAINT     S   ALTER TABLE ONLY public.shops
    ADD CONSTRAINT shops_pkey PRIMARY KEY (shop_id);
 :   ALTER TABLE ONLY public.shops DROP CONSTRAINT shops_pkey;
       public         postgres    false    203            �
           2606    33979    worker_info worker_info_pkey 
   CONSTRAINT     a   ALTER TABLE ONLY public.worker_info
    ADD CONSTRAINT worker_info_pkey PRIMARY KEY (worker_id);
 F   ALTER TABLE ONLY public.worker_info DROP CONSTRAINT worker_info_pkey;
       public         postgres    false    207            �
           2606    34019 +   order_of_books order_of_books_class_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.order_of_books
    ADD CONSTRAINT order_of_books_class_id_fkey FOREIGN KEY (class_id) REFERENCES public.class(class_id) ON UPDATE CASCADE ON DELETE CASCADE;
 U   ALTER TABLE ONLY public.order_of_books DROP CONSTRAINT order_of_books_class_id_fkey;
       public       postgres    false    2748    210    197            �
           2606    34009 ,   order_of_books order_of_books_client_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.order_of_books
    ADD CONSTRAINT order_of_books_client_id_fkey FOREIGN KEY (client_id) REFERENCES public.clients(client_id) ON UPDATE CASCADE ON DELETE CASCADE;
 V   ALTER TABLE ONLY public.order_of_books DROP CONSTRAINT order_of_books_client_id_fkey;
       public       postgres    false    201    2752    210            �
           2606    33999 .   order_of_books order_of_books_provider_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.order_of_books
    ADD CONSTRAINT order_of_books_provider_id_fkey FOREIGN KEY (provider_id) REFERENCES public.provider(provider_id) ON UPDATE CASCADE ON DELETE CASCADE;
 X   ALTER TABLE ONLY public.order_of_books DROP CONSTRAINT order_of_books_provider_id_fkey;
       public       postgres    false    205    2756    210            �
           2606    34004 *   order_of_books order_of_books_shop_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.order_of_books
    ADD CONSTRAINT order_of_books_shop_id_fkey FOREIGN KEY (shop_id) REFERENCES public.shops(shop_id) ON UPDATE CASCADE ON DELETE CASCADE;
 T   ALTER TABLE ONLY public.order_of_books DROP CONSTRAINT order_of_books_shop_id_fkey;
       public       postgres    false    210    2754    203            �
           2606    34014 ,   order_of_books order_of_books_worker_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.order_of_books
    ADD CONSTRAINT order_of_books_worker_id_fkey FOREIGN KEY (worker_id) REFERENCES public.worker_info(worker_id) ON UPDATE CASCADE ON DELETE CASCADE;
 V   ALTER TABLE ONLY public.order_of_books DROP CONSTRAINT order_of_books_worker_id_fkey;
       public       postgres    false    210    2758    207            �
           2606    34032 *   production production_book_identifier_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.production
    ADD CONSTRAINT production_book_identifier_fkey FOREIGN KEY (book_identifier) REFERENCES public.book(book_identifier) ON UPDATE CASCADE ON DELETE CASCADE;
 T   ALTER TABLE ONLY public.production DROP CONSTRAINT production_book_identifier_fkey;
       public       postgres    false    2750    211    199            �
           2606    34027 #   production production_order_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.production
    ADD CONSTRAINT production_order_id_fkey FOREIGN KEY (order_id) REFERENCES public.order_of_books(order_id) ON UPDATE CASCADE ON DELETE CASCADE;
 M   ALTER TABLE ONLY public.production DROP CONSTRAINT production_order_id_fkey;
       public       postgres    false    211    2762    210            �
           2606    33985    salary salary_worker_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.salary
    ADD CONSTRAINT salary_worker_id_fkey FOREIGN KEY (worker_id) REFERENCES public.worker_info(worker_id);
 F   ALTER TABLE ONLY public.salary DROP CONSTRAINT salary_worker_id_fkey;
       public       postgres    false    2758    207    208            �
           2606    34040    supply supply_provider_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.supply
    ADD CONSTRAINT supply_provider_id_fkey FOREIGN KEY (provider_id) REFERENCES public.provider(provider_id) ON UPDATE CASCADE ON DELETE CASCADE;
 H   ALTER TABLE ONLY public.supply DROP CONSTRAINT supply_provider_id_fkey;
       public       postgres    false    2756    212    205            P   �   x�M�Mn�0�דS� P�&6��"=?*,h+*u��T�("�'xs��!] Y������A��S��։C�n�	����:��$���^☣����S��hy��YWC}!�(N	��Z�/:���"y!y��n9�N���`�S�-��P;�)����byi�K3�{��H���#��#'g�c��y�q��'!J��K�n����`���]1T��7�_Y�U�M�H�=�P�=���e�ī��      N      x������ � �      R   �   x�U�;�@Dk�U������	�HCB� K�JQ`��7bL*K�̼q%8�CB\���t��6�M�zme��İ��W!:/8b�]E[�c�Ã���{�\���������E����4r$��`4�zܙ|Q�&����q9���;��o�      [      x������ � �      \      x������ � �      V   �   x���A� D�p
�*
��x�����՘��mI�F���	�qi~&�zo�f�0"��HC/��B�j�q�F`��Z���v*�f����1s����k��6C���c�u��N�4�r��-�^)k�O��	.�U'k�r|�����Br���r�      Y      x������ � �      T      x������ � �      ]   H   x�]��� C�3��R�	Huf��s �
ɧg�G`8�T'*��0n��?ͣ�l��Ov��=�ӝ�~��-��}      X     x�m�iN�0�ۧ��*�rS6	$
�R��B �I�r�y7b� Ԋ*���y/��Z4�a����H��kUA��,/�@��:|��,�R�X��M�0U�v�wj��
���*Ks�'�o�1!g�HtFJE����GW�����ޣ_�i�8a��gv��L��&�;F����Kb	���q0��$+J�K57����圍7r?�3ɜ�rC���Ȃ�<`t)�\���NGq�7~�{_n�"`+wD�.��*��_0n >1��8�gs���� �     