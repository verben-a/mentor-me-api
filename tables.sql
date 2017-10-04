create table users ( id serial PRIMARY KEY, 
	email varchar(128) unique not null, 
	password varchar(128) not null, 
	is_mentor boolean default false);

create table profile ( id serial PRIMARY KEY,
	user_id references users(id),
	name_surname varchar(100) not null,
	summary varchar(255) not null,
	position_at_company varchar(255),
	experience relationship experiences,
	);
	