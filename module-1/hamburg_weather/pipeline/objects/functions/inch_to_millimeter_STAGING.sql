CREATE OR ALTER FUNCTION STAGING_tasty_bytes.analytics.inch_to_millimeter(inch NUMBER(35,4))
  RETURNS NUMBER(35,4)
  AS
  $$
    inch * 25.4
  $$
;
