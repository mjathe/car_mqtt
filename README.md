# Communication in Smart Cars with MQTT

Dieses Konzept stellt die Interaktion/Kommunikation eines Fahrzeugs mit einer Smart City dar. Als Netzwerkprotokoll soll MQTT genutzt werden. Die im Fahrzeug befindlichen Sensoren(Clients) senden ihre Daten an einen lokalen Broker im Fahrzeug. Der lokale Broker fungiert dabei auch als Client des Smart City Brokers und leitet die gesammelten Daten in einer JSON Datei an den Smart City Broker weiter. Sollte die Verbindung zur Smart City unterbrochen sein, werden alle lokal gesammelt bis die Verbindung erneut aufgebaut wurde.

## Requirements
| ID |Description  |
|--|--|
|  FR A|The system must recognize disconnections.  |
| FR A.1|In case of disconnection the local broker has to store all incoming data.|
|NFR B | The system has a local MQTT broker in the Car.|
|FR C|The system has to guarantee that all data is sent to the online broker.|
|NFR D|The system uses MQTT for data transmission.|
|FR D|The system must send the collected data to the online broker after reconnecting|



## Sequence Diagram

![sequenceDiagram(UML/sequence_diagram.jpg)
