DELIMITER &&
CREATE PROCEDURE `details_customers`()
BEGIN
    DECLARE done INTEGER DEFAULT 0;
    DECLARE c_name VARCHAR(40);
    DECLARE c_city VARCHAR(35);
    DECLARE c_country VARCHAR(20);
    DECLARE c_grade DECIMAL(10,0);
    DECLARE customerDetails CURSOR for select CUST_NAME, CUST_CITY, CUST_COUNTRY, GRADE from customer where AGENT_CODE like 'A00%';
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done=1;
    OPEN customerDetails;
    get_details: LOOP
        FETCH customerDetails INTO c_name, c_city, c_country, c_grade;
        IF done=1 THEN
            LEAVE get_details;
        END IF;
    SELECT c_name, c_city, c_country, c_grade;
    END LOOP get_details;
    CLOSE customerDetails;
END&&
DELIMITER ;

CALL `details_customers`();
