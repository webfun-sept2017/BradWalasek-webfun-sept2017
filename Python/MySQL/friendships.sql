SELECT clients.client_id AS Client_id, created_datetime FROM clients
JOIN sites ON clients.client_id = sites.client_id
WHERE clients.client_id = 1
GROUP BY created_datetime