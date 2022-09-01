DELIMITER &&
CREATE PROCEDURE `customerLivingInTheCityNames`(IN city VARCHAR(50))
BEGIN
    select CUST_NAME from customer where WORKING_AREA = city;
END&&
DELIMITER ;

CALL `customerLivingInTheCityNames`("Bangalore");
