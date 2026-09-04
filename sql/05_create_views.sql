-- View: appointments by status

CREATE OR REPLACE VIEW analytics.vw_appointments_by_status AS
SELECT
    status,
    COUNT(*) AS total_appointments
FROM harmonized.appointments
GROUP BY status
ORDER BY total_appointments DESC;

SELECT * FROM analytics.vw_appointments_by_status;