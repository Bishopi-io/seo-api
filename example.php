<?php

$url = "https://api.bishopi.io/domain_seo_analysis/?domain=bishopi.io";

// Initialize a cURL session
$ch = curl_init($url);

// Set the Authorization header
$headers = [
    'Authorization: Api-Key 1234'
];
curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);

// Set the option to return the response as a string
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

// Execute the request
$response = curl_exec($ch);

// Check for errors
if ($response === false) {
    $error = curl_error($ch);
    curl_close($ch);
    die('Error making request: ' . $error);
}

// Close the cURL session
curl_close($ch);

// Print the response
echo $response;
?>
