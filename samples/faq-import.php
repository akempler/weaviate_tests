<?php

# Store a single object.
# run locally with:
# php -S localhost:8090
# Then access at http://localhost:8090/faq-import.php
# See document-schema.py.

use GuzzleHttp\Client;
use GuzzleHttp\Request;

require __DIR__ . '/vendor/autoload.php';

$client = new Client();

$headers = [
  'Content-Type' => 'application/json',
  'auth' => ['Bearer' => 'akemplerkey'],
];
$body = '{
  "class": "Faq",
  "properties": {
    "title": "Are service animals allowed in the courts?",
    "category": "ADA Accessiblity",
    "textVector": "Yes, Colorado law, section 24-34-803, C.R.S., provides that a person with a disability has the right to be accompanied by a service animal specially trained for that person as a reasonable accommodation or a trainer of a service animal, or an individual with a disability accompanied by an animal that is being trained to be a service animal, has the right to be accompanied by the service animal in training. The service animal or service animal in training must be permitted to accompany the individual with a disability or trainer to all areas of the facility where customers are normally allowed to go. An individual with a service animal or service animal in training may not be segregated from other customers. The care and supervision of the service animal is the sole responsibility of the owner. The court is not required to provide care, food or a special location for the animal."
  }
}';
$request = new \GuzzleHttp\Psr7\Request('POST', 'http://localhost:8080/v1/objects?consistency_level=ALL', $headers, $body);
$res = $client->sendAsync($request)->wait();
echo $res->getBody();


$headers = [
  'Content-Type' => 'application/json'
];
$body = '{
  "class": "Faq",
  "properties": {
    "filename": "Can Probation be transferred to another state?",
    "category": "Probation",
    "textVector": "Yes. Colorado participates in the Interstate Compact for Adult Offender Supervision and the Interstate Compact for Juveniles which govern the movement of offenders between states. There are very specific requirements that must be met before anyone convicted of a felony, certain misdemeanors or adjudicated a delinquent will be allowed to move from the state. Generally, we cannot allow someone on Probation to move to another state without the consent of the other state. Talk to your Probation Officer about the requirements and the process. Your Probation Officer must approve of the move and you must apply to the other state through our office and be accepted by them prior to moving."
  }
}';
$request = new \GuzzleHttp\Psr7\Request('POST', 'http://localhost:8080/v1/objects?consistency_level=ALL', $headers, $body);
$res = $client->sendAsync($request)->wait();
echo $res->getBody();

$headers = [
  'Content-Type' => 'application/json'
];
$body = '{
  "class": "Faq",
  "properties": {
    "filename": "How can I file a complaint against a judge?",
    "category": "General",
    "textVector": "To file a complaint against a judge, contact the Judicial Discipline Commission: Phone: 303-457-5131, Fax: 303-501-1143"
  }
}';
$request = new \GuzzleHttp\Psr7\Request('POST', 'http://localhost:8080/v1/objects?consistency_level=ALL', $headers, $body);
$res = $client->sendAsync($request)->wait();
echo $res->getBody();
