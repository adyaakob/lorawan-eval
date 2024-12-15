# **Evaluation Procedure for LoRaWAN-based Real-time Worker Tracking System in Remote Oil Palm Plantations**

This document outlines a comprehensive evaluation procedure for the LoRaWAN-based real-time worker tracking system proposed by TEQ Armada Sdn Bhd to Sabah Softwoods Berhad. The evaluation focuses on assessing the feasibility and performance of the system using alternative equipment due to the unavailability of the proposed devices.

## **Evaluation Equipment**

* **End-user devices:** Dragino Tracker D LoRaWAN GPS trackers 1  
* **Gateway:** Dragino Outdoor Gateway DL0S86 (AS923) with 4G EC25 2  
* **Tools/Equipment:**  
  * Laptop with LoRaWAN network server and mapping software (e.g., The Things Network with ChirpStack, with mapping software like QGIS)  
  * High-accuracy GPS device (e.g., Garmin GPSMAP 66i) or detailed map of the estate  
  * Cellular signal strength meter (e.g., RF Explorer Handheld Spectrum Analyzer) or mobile phone with field test mode  
  * Measuring tape or laser distance measuring equipment (e.g., Bosch GLM 50 C)  
  * Tools for mounting the gateway (e.g., ladder, mounting brackets, appropriate tools for the chosen mounting surface)

## **Test Location**

The evaluation will be conducted in **one** oil palm estate in Sabah, Malaysia, selected by the tester from the following list:

1. Mawang  
2. Sg Tiagau  
3. Bukit Tuok  
4. Kumani  
5. Kapilit  
6. Sg Indit  
7. Banita  
8. Cenderamata  
9. Dumpas

**Selected Estate:**

(Enter the name of the selected estate here)

## **Evaluation Procedure**

This procedure outlines a series of tests to evaluate the performance of the LoRaWAN-based worker tracking system. Each test includes a form to record observations and measurements.

**Test 1: LoRaWAN Range and Coverage**

**Objective:** To determine the effective range of the LoRaWAN network in the oil palm plantation environment.

**Procedure:**

1. Deploy the Dragino DL0S86 gateway at a central location within the selected estate. Record the gateway's GPS coordinates.  
2. Starting with the tracker device near the gateway, record the Received Signal Strength Indicator (RSSI) and any packet loss.  
3. Place Dragino Tracker D devices at various distances from the gateway (e.g., 100m, 500m, 1km, 2km, 5km) in different directions. Record the GPS coordinates of each tracker.  
4. Vary the terrain and vegetation density between the gateway and tracker devices (e.g., open areas, dense foliage, near buildings, different elevations).  
5. For each location, record the signal strength (RSSI) and packet loss. Note the Spreading Factor (SF) used for communication.  
6. Observe and record the time it takes for data to be transmitted from the tracker to the gateway (latency).

**Form (Part 1):**

| Test Number | Tracker ID | Distance to Gateway (m) | Tracker GPS Coordinates |
| :---- | :---- | :---- | :---- |
| 1.1 |  |  |  |
| 1.2 |  |  |  |
| 1.3 |  |  |  |
| 1.4 |  |  |  |
| 1.5 |  |  |  |

**Form (Part 2):**

| Test Number | RSSI (dBm) | SF | Packet Loss (%) | Latency (s) | Notes (Terrain, Obstructions, etc.) |
| :---- | :---- | :---- | :---- | :---- | :---- |
| 1.1 |  |  |  |  |  |
| 1.2 |  |  |  |  |  |
| 1.3 |  |  |  |  |  |
| 1.4 |  |  |  |  |  |
| 1.5 |  |  |  |  |  |
| 1.6 |  |  |  |  |  |
| 1.7 |  |  |  |  |  |
| 1.8 |  |  |  |  |  |
| 1.9 |  |  |  |  |  |
| 1.10 |  |  |  |  |  |

**Test 2: GPS Performance Under Canopy**

**Objective:** To evaluate the accuracy and reliability of GPS positioning under the dense canopy of oil palm trees.

**Procedure:**

1. Place Dragino Tracker D devices at different locations under the canopy with varying densities (e.g., dense foliage, moderate foliage, edge of the canopy).  
2. Record the GPS coordinates obtained by the tracker devices.  
3. Compare the recorded coordinates with the actual coordinates obtained using a high-accuracy GPS device or a detailed map.  
4. Calculate the positional error (distance between recorded and actual coordinates) and analyze the variations in accuracy based on canopy density.  
5. Repeat the test at different times of the day to assess the impact of satellite availability.

**Form (Part 1):**

| Test Number | Tracker ID | Canopy Density | Recorded Coordinates | Actual Coordinates |
| :---- | :---- | :---- | :---- | :---- |
| 2.1 |  |  |  |  |
| 2.2 |  |  |  |  |
| 2.3 |  |  |  |  |
| 2.4 |  |  |  |  |
| 2.5 |  |  |  |  |

**Form (Part 2):**

| Test Number | Positional Error (m) | Time of Day | Notes (e.g., weather conditions) |
| :---- | :---- | :---- | :---- |
| 2.1 |  |  |  |
| 2.2 |  |  |  |
| 2.3 |  |  |  |
| 2.4 |  |  |  |
| 2.5 |  |  |  |
| 2.6 |  |  |  |
| 2.7 |  |  |  |
| 2.8 |  |  |  |
| 2.9 |  |  |  |
| 2.10 |  |  |  |

**Test 3: Device Performance and Battery Life**

**Objective:** To assess the performance of the Dragino Tracker D in terms of data transmission, battery life, and overall functionality.

**Procedure:**

1. Fully charge the battery of each Dragino Tracker D device.  
2. Configure the Dragino Tracker D to transmit data at different intervals (e.g., every 1 minute, 5 minutes, 15 minutes).  
3. For each interval, monitor and record the data transmission rate and packet loss.  
4. Record the time taken for the battery to deplete under each data transmission interval.  
5. Observe and document any issues related to device functionality, such as GPS signal acquisition, data logging, or sensor readings.

**Form:**

| Test Number | Tracker ID | Data Transmission Interval (min) | Data Transmission Rate | Packet Loss (%) | Battery Life (hours) | Functional Issues | Notes |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| 3.1 |  |  |  |  |  |  |  |
| 3.2 |  |  |  |  |  |  |  |
| 3.3 |  |  |  |  |  |  |  |

**Test 4: Cellular Signal Strength**

**Objective:** To measure cellular signal strength across the selected estate to identify optimal gateway placement for reliable backhaul connectivity.

**Procedure:**

1. Use a cellular signal strength meter or a mobile phone with a field test mode to measure signal strength (RSRP) at various locations within the estate.  
2. Record the signal strength (RSRP in dBm), network provider, and GPS coordinates for each location.  
3. Identify areas with weak or no cellular coverage.  
4. Analyze the data to determine the best locations for gateway deployment to ensure reliable cellular backhaul.

**Form (Part 1):**

| Test Number | Location Coordinates | CelcomDigi | Maxis | U Mobile | unifi | Yes 4G |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| 4.1 |  |  |  |  |  |  |
| 4.2 |  |  |  |  |  |  |
| 4.3 |  |  |  |  |  |  |
| 4.4 |  |  |  |  |  |  |
| 4.5 |  |  |  |  |  |  |

**Form (Part 2):**

| Test Number | RSRP (dBm) | Notes |
| :---- | :---- | :---- |
| 4.1 |  |  |
| 4.2 |  |  |
| 4.3 |  |  |
| 4.4 |  |  |
| 4.5 |  |  |
| 4.6 |  |  |
| 4.7 |  |  |
| 4.8 |  |  |
| 4.9 |  |  |
| 4.10 |  |  |

## **Data Analysis and Reporting**

After completing the evaluation tests, analyze the collected data to assess the performance of the LoRaWAN-based worker tracking system. Consider the following factors:

* **LoRaWAN coverage and signal strength:** Evaluate the network's ability to provide reliable communication across the estate, considering terrain and vegetation. Analyze the impact of distance, Spreading Factor, and obstacles on signal quality and packet loss.  
* **GPS accuracy under canopy:** Determine the level of accuracy achievable for worker location tracking under the oil palm canopy. Analyze the variations in accuracy based on canopy density and time of day.  
* **Device performance and battery life:** Assess the tracker's functionality, data transmission capabilities, and battery life in the field. Analyze the relationship between data transmission intervals and battery life.  
* **Cellular signal strength:** Identify areas with limited cellular coverage and determine the optimal gateway placement for reliable backhaul connectivity. Evaluate the signal strength of different cellular providers to identify the best option for the estate.

Compile the findings into a comprehensive report that includes:

* **Executive summary:** A concise overview of the evaluation objectives, methodology, and key findings.  
* **Detailed test results:** Present the data collected from each test, including tables, charts, and maps (if available).  
* **Analysis and discussion:** Interpret the results, discuss the implications for system design and deployment, and address any limitations or challenges encountered.  
* **Recommendations:** Provide recommendations for optimizing network deployment, selecting appropriate equipment, and mitigating potential challenges.  
* **Conclusion:** Summarize the overall feasibility and effectiveness of the LoRaWAN-based worker tracking system for Sabah Softwoods Berhad.

## **Compromises and Limitations**

Acknowledge the compromises and limitations associated with using the alternative evaluation equipment:

* **GPS Accuracy:** The HKT GT-100 may offer better accuracy due to its dual-frequency band reception and anti-jamming capabilities.  
* **Feature Set:** The Dragino Tracker D includes additional features that may affect battery life and performance comparisons.  
* **Ruggedness:** The Dragino devices may have different ruggedness specifications compared to the proposed equipment.  
* **Power Source:** The Dragino gateway relies on a DC power supply, while the proposed gateway is solar-powered.

It's crucial to consider these limitations when interpreting the evaluation results and extrapolating them to the proposed system.

## **Scope of Evaluation**

This evaluation plan focuses on assessing the feasibility of the LoRaWAN-based worker tracking system in terms of network coverage, GPS performance, and device functionality. Integration with the end-user dashboard and application server is beyond the scope of this evaluation.

#### **Works cited**

1\. TrackerD \-- LoRaWAN Tracker User Manual \- Dragino Wiki, accessed on December 14, 2024, [https://wiki.dragino.com/xwiki/bin/view/Main/User%20Manual%20for%20LoRaWAN%20End%20Nodes/TrackerD/](https://wiki.dragino.com/xwiki/bin/view/Main/User%20Manual%20for%20LoRaWAN%20End%20Nodes/TrackerD/)  
2\. DLOS8 Outdoor LoRaWAN Gateway \- Dragino, accessed on December 15, 2024, [https://www.dragino.com/products/lora-lorawan-gateway/item/160-dlos8.html](https://www.dragino.com/products/lora-lorawan-gateway/item/160-dlos8.html)
