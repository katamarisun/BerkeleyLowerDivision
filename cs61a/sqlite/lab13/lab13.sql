.read data.sql

-- Q1
create table flight_costs as
  with prices(day, today, next, third) as (
    select 1, 20, 30, 40 union
    select day + 1, next, third, 5 * ((day + 3) % 7) + (third + next) / 2 from prices where day < 25

    )
  select day, today from prices;

-- Q2
create table schedule as
  with helper(route, current, cost, count, total) as (
    select "SFO", "SFO", 0, 0, 0 union
    select route || ", " || arrival, arrival, price, count + 1, total + price from helper, flights where current = departure and count < 2
    )
  select route, total from helper where current = "PDX" order by total;

-- Q3
create table shopping_cart as
  with helper(groceries, last, leftover) as (
    select item, price, 60 - price from supermarket where 60 - price >= 0 union
    select groceries || ", " || item, price, leftover - price from helper, supermarket where leftover - price >= 0 and last <= price
    )
  select groceries, leftover from helper order by leftover asc, groceries;

-- Q4
create table number_of_options as
  with num(counts) as (
    select count(*) from main_course group by meat
    )
  select count(*) from num;

-- Q5
create table calories as
  select count(*) from main_course as a, pies as b where a.calories + b.calories < 2500;

-- Q6
create table healthiest_meats as
  with meals(meat, calories) as (
    select meat, a.calories + b.calories from main_course as a, pies as b
    )
  select meat, min(calories) from meals group by meat having max(calories) <= 3000 ;

-- Q7
create table average_prices as
  select category, avg(MSRP) from products group by category;

-- Q8
create table lowest_prices as
  select item, store, min(price) as prices from inventory group by item;

-- Q9
create table shopping_list as
  select item, store as store from lowest_prices, products where item = name 
  group by category having min(MSRP / rating);

-- Q10
create table total_bandwidth as
  select sum(Mbs) from shopping_list as a, stores as b where a.store = b.store ;
