<?php

# Store a single object.
# run locally with:
# php -S localhost:8090
# Then access at http://localhost:8090/document-import.php
# See document-schema.py.

use GuzzleHttp\Client;
use GuzzleHttp\Request;

require __DIR__ . '/vendor/autoload.php';

$client = new Client();

$headers = [
  'Content-Type' => 'application/json'
];
$body = '{
  "class": "JudicialDocument",
  "properties": {
    "filename": "somefile2.pdf",
    "name": "Some File 2",
    "category": "Affidavit",
    "textVector": "Four cats and a dog are a lot for a small appartment."
  }
}';
$request = new \GuzzleHttp\Psr7\Request('POST', 'http://localhost:8080/v1/objects?consistency_level=ALL', $headers, $body);
$res = $client->sendAsync($request)->wait();
echo $res->getBody();


$headers = [
  'Content-Type' => 'application/json'
];
$body = '{
  "class": "JudicialDocument",
  "properties": {
    "filename": "somefile.pdf",
    "name": "Some File",
    "category": "Affidavit",
    "textVector": "This is a test of the emergency broadcast system. This is only a test."
  }
}';
$request = new \GuzzleHttp\Psr7\Request('POST', 'http://localhost:8080/v1/objects?consistency_level=ALL', $headers, $body);
$res = $client->sendAsync($request)->wait();
echo $res->getBody();
