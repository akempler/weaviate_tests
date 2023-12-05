<?php
# https://github.com/timkley/weaviate-php

# Store a single object.
# run locally with:
# php -S localhost:8090
# Then access at http://localhost:8090/document-get.php
# See document-schema.py.

// use GuzzleHttp\Client;
// use GuzzleHttp\Request;

require __DIR__ . '/vendor/autoload.php';

// $client = new Client();

use Weaviate\Weaviate;

$weaviate = new Weaviate('http://localhost:8080/v1', '');

$response = $weaviate->graphql()->get('{
  Get {
    JudicialDocument {
      name
      category
    }
  }
}');


// $headers = [
//   'Content-Type' => 'application/json'
// ];


// $body = '{
//   Get {
//     JudicialDocument (
//       limit: 1
//     ) {
//       name
//     }
//   }
// }';

print('Sending request...' . PHP_EOL);

echo "<pre>";
echo var_dump($response);
echo "</pre>";
