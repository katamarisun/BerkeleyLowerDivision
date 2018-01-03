create table parents as
  select "abraham" as parent, "barack" as child union
  select "abraham"          , "clinton"         union
  select "delano"           , "herbert"         union
  select "fillmore"         , "abraham"         union
  select "fillmore"         , "delano"          union
  select "fillmore"         , "grover"          union
  select "eisenhower"       , "fillmore";

create table dogs as
  select "abraham" as name, "long" as fur, 26 as height union
  select "barack"         , "short"      , 52           union
  select "clinton"        , "long"       , 47           union
  select "delano"         , "long"       , 46           union
  select "eisenhower"     , "short"      , 35           union
  select "fillmore"       , "curly"      , 32           union
  select "grover"         , "short"      , 28           union
  select "herbert"        , "curly"      , 31;

create table sizes as
  select "toy" as size, 24 as min, 28 as max union
  select "mini",        28,        35        union
  select "medium",      35,        45        union
  select "standard",    45,        60;

-------------------------------------------------------------
-- PLEASE DO NOT CHANGE ANY SQL STATEMENTS ABOVE THIS LINE --
-------------------------------------------------------------

-- The size of each dog
create table size_of_dogs as
  select name, size from dogs, sizes where sizes.min < dogs.height and dogs.height <= sizes.max;

-- All dogs with parents ordered by decreasing height of their parent
create table by_height as 
  select a.name from dogs as a, parents, dogs as b where a.name = parents.child and parents.parent = b.name order by b.height desc;

-- Sentences about siblings that are the same size
create table sentences as
    with siblings(name1, name2, size) as (
      select a.child, b.child, c.size from parents as a, parents as b, size_of_dogs as c, size_of_dogs as d
          where a.parent = b.parent and a.child < b.child and a.child = c.name and b.child = d.name and c.size = d.size


      )
  select name1 || " and " || name2 || " are " || size || " siblings" from siblings;

-- Ways to stack 4 dogs to a height of at least 170, ordered by total height
create table stacks as
  with meow(stack, last, count, total) as (
    select name, height, 1, height from dogs union
    select stack || ", " || name, height, count + 1, height + total from meow, dogs where count < 4 and height > last

    )
  select stack, total from meow where total > 170 order by total;

-- non_parents is an optional, but recommended question
-- All non-parent relations ordered by height difference
create table non_parents as
  with grand(grandparents, size1, grandchildren, size2) as (
    select a.name, a.height, b.name, b.height from dogs as a, dogs as b, parents as c, parents as d 
  where a.name = c.child 
  and b.name != c.parent and b.name = d.child and a.name != d.parent
    )
  select grandparents, grandchildren from grand where size1 > size2;

create table ints as
    with i(n) as (
        select 1 union
        select n+1 from i limit 100
    )
    select n from i;

create table divisors as
    with integers(x) as (
      select * from ints)
    select a.x as num, count(b.x) as amount from integers as a, integers as b where a.x % b.x = 0 group by a.x;

create table primes as
    select num from divisors where amount = 2 and num != 1;
