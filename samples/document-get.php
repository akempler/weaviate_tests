<?php

# Store a single object.
# run locally with:
# php -S localhost:8090
# Then access at http://localhost:8090/document-get.php
# See document-schema.py.

use GuzzleHttp\Client;
use GuzzleHttp\Request;

require __DIR__ . '/vendor/autoload.php';

$client = new Client();

$headers = [
  'Content-Type' => 'application/json'
];


$body = '{
  Get {
    JudicialDocument (
      limit: 1
    ) {
      name
    }
  }
}';

$headers = [
  'Content-Type' => 'application/json'
];

print('Sending request...' . PHP_EOL);

$request = new \GuzzleHttp\Psr7\Request('GET', 'http://localhost:8080', $headers, $body);
//$request = new \GuzzleHttp\Psr7\Request('POST', 'http://localhost:8080/v1/objects?consistency_level=ALL', $headers, $body);
$res = $client->sendAsync($request)->wait();

echo "<pre>";
echo $res->getBody();
echo "</pre>";
