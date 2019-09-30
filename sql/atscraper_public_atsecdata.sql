create table atsecdata
(
	id bigint default nextval('increment_2'::regclass) not null
		constraint atsecdata_pkey
			primary key,
	article_id bigint not null,
	sec_id varchar,
	created_at varchar(225),
	updated_at timestamp
)
;

-- INSERT INTO public.atsecdata (id, article_id, sec_id, created_at, updated_at) VALUES (2661, 44, '25-8-2019 18:26:25', '443', null);
-- INSERT INTO public.atsecdata (id, article_id, sec_id, created_at, updated_at) VALUES (2662, 44, '25-8-2019 18:58:23', '443', null);
-- INSERT INTO public.atsecdata (id, article_id, sec_id, created_at, updated_at) VALUES (2663, 44, '25-8-2019 19:0:39', '443', null);
-- INSERT INTO public.atsecdata (id, article_id, sec_id, created_at, updated_at) VALUES (2664, 44, '25-8-2019 19:4:12', '443', null);
-- INSERT INTO public.atsecdata (id, article_id, sec_id, created_at, updated_at) VALUES (2665, 44, '2019-8-25 19:5:38', '443', null);
-- INSERT INTO public.atsecdata (id, article_id, sec_id, created_at, updated_at) VALUES (2666, 44, '2019-8-25 19:5:50', '443', null);
-- INSERT INTO public.atsecdata (id, article_id, sec_id, created_at, updated_at) VALUES (2667, 44, '2019-8-25 19:7:54', '443', null);
-- INSERT INTO public.atsecdata (id, article_id, sec_id, created_at, updated_at) VALUES (2668, 44, '2019-8-25 19:8:12', '443', null);
-- INSERT INTO public.atsecdata (id, article_id, sec_id, created_at, updated_at) VALUES (2669, 44, '2019-8-25 19:8:27', '443', null);
-- INSERT INTO public.atsecdata (id, article_id, sec_id, created_at, updated_at) VALUES (2670, 44, '2019-8-25 19:9:20', '443', null);
-- INSERT INTO public.atsecdata (id, article_id, sec_id, created_at, updated_at) VALUES (2671, 44, '2019-8-25 19:9:46', '443', null);
-- INSERT INTO public.atsecdata (id, article_id, sec_id, created_at, updated_at) VALUES (2672, 44, '2019-8-25 19:10:19', '443', null);
-- INSERT INTO public.atsecdata (id, article_id, sec_id, created_at, updated_at) VALUES (2673, 44, '2019-8-25 19:11:17', '443', null);
-- INSERT INTO public.atsecdata (id, article_id, sec_id, created_at, updated_at) VALUES (2674, 44, '2019-8-25 19:17:3', '443', null);
-- INSERT INTO public.atsecdata (id, article_id, sec_id, created_at, updated_at) VALUES (2675, 44, '2019-8-25 19:18:39', '443', null);
-- INSERT INTO public.atsecdata (id, article_id, sec_id, created_at, updated_at) VALUES (2676, 44, '2019-8-25 19:21:9', '443', null);
-- INSERT INTO public.atsecdata (id, article_id, sec_id, created_at, updated_at) VALUES (2677, 44, '2019-8-25 19:21:27', '443', null);
-- INSERT INTO public.atsecdata (id, article_id, sec_id, created_at, updated_at) VALUES (2678, 44, '2019-8-25 19:21:52', '443', null);
-- INSERT INTO public.atsecdata (id, article_id, sec_id, created_at, updated_at) VALUES (2679, 44, '2019-8-25 19:22:47', '443', null);
-- INSERT INTO public.atsecdata (id, article_id, sec_id, created_at, updated_at) VALUES (2680, 44, '2019-8-25 19:25:38', '443', null);
-- INSERT INTO public.atsecdata (id, article_id, sec_id, created_at, updated_at) VALUES (2681, 44, '2019-8-25 19:25:49', '443', null);
-- INSERT INTO public.atsecdata (id, article_id, sec_id, created_at, updated_at) VALUES (2682, 44, '2019-8-25 19:28:27', '443', null);
-- INSERT INTO public.atsecdata (id, article_id, sec_id, created_at, updated_at) VALUES (2683, 44, '2019-8-25 19:31:9', '443', null);
-- INSERT INTO public.atsecdata (id, article_id, sec_id, created_at, updated_at) VALUES (2684, 44, '2019-8-25 19:31:43', '443', null);