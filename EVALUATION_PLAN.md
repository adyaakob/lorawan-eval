# **Evaluation of LoRaWAN-based Real-time Worker Tracking System in Remote Oil Palm Plantations**

This report outlines the evaluation plan for a LoRaWAN-based real-time worker tracking system proposed by TEQ Armada Sdn Bhd to Sabah Softwoods Berhad (softwood.com.my). It details the project background, user requirements, proposed system architecture, and the rationale for selecting specific devices for the evaluation.

## **Project Background**

This project aims to enhance worker safety and optimize operational efficiency in Sabah Softwoods Berhad's oil palm plantations. Traditional tracking methods are inadequate due to the vast, densely vegetated areas and limitations of GPS and cellular signals under the palm canopy. This LoRaWAN-based system seeks to overcome these challenges by providing real-time worker location data and reliable communication, even in areas with limited cellular coverage.

## **Key Requirements**

* **Real-time tracking:** Continuous monitoring of 4,500 workers across nine estates (Mawang, Sg Tiagau, Bukit Tuok, Kumani, Kapilit, Sg Indit, Banita, Cenderamata, and Dumpas).  
* **Technology:** Utilize LoRaWAN technology for its long-range coverage (up to 10km in rural areas) 1, low power consumption, and ability to penetrate dense foliage.  
* **Infrastructure:** Deploy solar-powered LoRaWAN gateways for sustainable operation.  
* **Integration:** Ensure seamless integration with existing HQ management systems for data analysis and reporting.  
* **Overcome cellular limitations:** Address limited cellular coverage in Sabah's remote areas by providing reliable communication through the LoRaWAN network.

## **System Purpose**

* **Enhanced safety:** Real-time location tracking enables immediate response to emergencies and accidents.  
* **Improved response times:** Faster response to worker distress calls and incidents.  
* **Optimized workforce management:** Efficient allocation of workers and improved task management.  
* **Data-driven insights:** Generate data for performance analysis, identifying areas for improvement in safety and efficiency.

## **Proposed System**

The proposed system comprises:

* **End-user devices:** HKT GT-100 LoRaWAN GPS trackers 1  
* **Gateway:** Milesight SG50 LoRaWAN gateway 8  
* **Network Server:** A LoRaWAN network server for managing devices and data.  
* **Application Server:** A platform for visualizing worker location data, generating reports, and triggering alerts.

## **Equipment for Evaluation**

Due to the unavailability of the proposed HKT GT-100 trackers for immediate field evaluation, alternative devices will be used to gather preliminary data and assess the feasibility of the system. The following equipment will be used for the evaluation:

* **End-user devices:** Dragino Tracker D LoRaWAN GPS trackers 2  
* **Gateway:** Dragino Outdoor Gateway DL0S86 (AS923) with 4G EC25 3

## **Compromises with Evaluation Equipment**

Utilizing the Dragino Tracker D and DL0S86 gateway for evaluation introduces certain compromises:

* **GPS Accuracy:** The HKT GT-100 may offer better accuracy due to its dual-frequency band reception (L1 and L5) and anti-jamming capabilities 4. The Dragino Tracker D relies solely on GPS and BLE positioning 5.  
* **Feature Set:** The Dragino Tracker D includes additional features like Wi-Fi, Bluetooth 4.2, motion detection, and temperature/humidity sensors 2, which are not present in the HKT GT-100. These differences could affect battery life and performance comparisons.  
* **Ruggedness:** The HKT GT-100 has an IP67 waterproof rating 9, while the Dragino Tracker D's ruggedness specifications are not explicitly stated. Similarly, the Milesight SG50 gateway has an IP67 rating, while the Dragino DL0S86 gateway's ruggedness is not specified. This difference might affect the long-term durability and reliability of the devices in harsh plantation environments.  
* **Power Source:** The Milesight SG50 is designed for solar power with battery backup, while the Dragino DL0S86 relies on a 5V, 2A DC power supply. This difference could impact the sustainability and maintenance requirements of the deployed system.

It's important to acknowledge these limitations when interpreting the evaluation results and extrapolating them to the proposed HKT GT-100 and Milesight SG50.

## **Key Characteristics/Specifications**

To further highlight the differences, here's a comparison table:

**End-user Devices**

| Feature | HKT GT-100 | Dragino Tracker D |
| :---- | :---- | :---- |
| **Positioning Technology** | GPS (L1 & L5) 4 | GPS 5 |
| **Ruggedness** | IP67 9 | Not specified |
| **Battery Life** | 1000 mAh Li-ion 1 | 1000 mAh Li-ion 2 |
| **Extra Features** | Bluetooth 4.0 1 | Wi-Fi, Bluetooth 4.2, Motion Detection, Temperature/Humidity Sensors 2 |
| **Dimensions** | 100 x 33 x 20 mm 6 | 85 x 48 x 15 mm 7 |
| **Operating Temperature** | \-20°C to 65°C 1 | \-40°C to 60°C 2 |

**Gateways**

| Feature | Milesight SG50 | Dragino DL0S86 (AS923) with 4G EC25 |
| :---- | :---- | :---- |
| **Ingress Protection** | IP67 | Not specified |
| **Power Source** | Solar/DC/Battery | 5V, 2A DC |
| **Operating Temperature** | \-30°C to \+70°C | \-20°C to 70°C |
| **Antenna** | External | Not specified |
| **Channels** | 8 (Half-duplex) 8 | Not specified |
| **Backhaul** | 4G LTE (CAT 1)/GSM | 4G LTE |

## **8-Channel Parallel Processing of Milesight SG50**

The Milesight SG50 gateway supports 8-channel parallel processing, enabling it to handle a higher volume of data and support more than 2,000 end-node connections simultaneously. This feature is crucial for the proposed worker tracking system, as it needs to manage a large number of devices (4,500) across the nine estates. The 8-channel capacity ensures efficient data transmission and minimizes potential bottlenecks in the network.

## **Rationale for Selecting Evaluation Equipment**

Despite the compromises, the Dragino Tracker D and Dragino DL0S86 gateway were chosen for their availability and suitability for the project's core objectives:

**Dragino Tracker D:**

* **LoRaWAN compatibility:** Supports LoRaWAN, allowing for assessment of network coverage and signal strength in the plantation environment 2.  
* **GPS functionality:** Enables evaluation of GPS performance under canopy, a critical requirement for the project 5.  
* **Open-source nature:** Allows for potential customization and flexibility in testing different configurations 2.

**Dragino DL0S86 Gateway:**

* **LoRaWAN support:** Provides LoRaWAN connectivity for the Dragino Tracker D devices.  
* **4G backhaul:** Offers cellular connectivity for data backhaul in remote locations.

## **Evaluation Objectives**

The primary objectives of the field evaluation are:

* **Assess LoRaWAN range and coverage:** Determine the effective range of the LoRaWAN network in the oil palm plantation environment, considering factors like terrain, vegetation density, and interference.  
* **Evaluate GPS performance under canopy:** Analyze the accuracy and reliability of GPS positioning under the dense canopy of oil palm trees.  
* **Gather data on device performance:** Collect information on device battery life, data transmission rates, and overall functionality in the field.  
* **Evaluate cellular signal strength:** Measure cellular signal strength across the nine estates to identify optimal gateway placement for reliable backhaul connectivity. This will help determine if LoRaWAN can effectively overcome cellular limitations in the area.  
* **Assess end-device battery life:** Determine the battery life of the Dragino Tracker D under typical usage conditions in the plantation environment, considering factors like data transmission frequency and GPS usage. This will provide insights into the expected battery life of the HKT GT-100, taking into account the differences in features and power consumption.

## **Geographical Considerations**

The nine estates are located in remote areas of Sabah, known for their varied terrain, dense vegetation, and potential limitations in cellular coverage. The evaluation plan will consider these factors:

* **Terrain:** The terrain may vary across the estates, including hilly areas, valleys, and potentially dense foliage. This can affect signal propagation and device performance.  
* **Vegetation:** The dense canopy of oil palm trees can significantly impact GPS accuracy and LoRaWAN signal strength.  
* **Cellular Coverage:** Cellular signal strength may be limited in some areas, requiring careful consideration of gateway placement for reliable backhaul connectivity.

## **Scope of Evaluation**

This evaluation plan focuses on assessing the feasibility of the LoRaWAN-based worker tracking system in terms of network coverage, GPS performance, and device functionality. Integration with the end-user dashboard and application server is beyond the scope of this evaluation.

## **Expected Outcomes**

The evaluation is expected to provide valuable insights into the feasibility of the proposed LoRaWAN-based worker tracking system. The data gathered will be used to:

* **Optimize network deployment:** Determine the optimal placement and number of gateways required for complete coverage of the plantation.  
* **Assess device suitability:** Evaluate the performance of the Dragino Tracker D and extrapolate the findings to the proposed HKT GT-100, considering the differences in specifications and features.  
* **Identify potential challenges:** Identify any potential challenges related to signal propagation, device performance, or environmental factors that may need to be addressed during the full-scale implementation.  
* **Validate LoRaWAN's effectiveness:** Confirm if LoRaWAN can effectively overcome GPS and cellular limitations in the targeted oil palm plantations.

## **Conclusion**

This evaluation plan outlines the key aspects of the field evaluation for the LoRaWAN-based worker tracking system. By utilizing the Dragino Tracker D and Dragino DL0S86 gateway, the project can gather preliminary data and assess the feasibility of the system before proceeding with the full-scale deployment of the HKT GT-100 and Milesight SG50 gateway. The findings from the evaluation will be crucial in optimizing the system design and ensuring its successful implementation to enhance worker safety and operational efficiency in the oil palm plantations.

#### **Works cited**

1\. LoRaWAN GPS Tracker \- Hunan HKT Technology Co., Ltd., accessed on December 14, 2024, [https://www.hktlora.com/product/lorawan-gps-tracker/](https://www.hktlora.com/product/lorawan-gps-tracker/)  
2\. TrackerD \-- LoRaWAN Tracker \- Dragino, accessed on December 14, 2024, [https://www.dragino.com/products/tracker/item/234-trackerd.html](https://www.dragino.com/products/tracker/item/234-trackerd.html)  
3\. DLOS8 Outdoor LoRaWAN Gateway \- Dragino, accessed on December 15, 2024, [https://www.dragino.com/products/lora-lorawan-gateway/item/160-dlos8.html](https://www.dragino.com/products/lora-lorawan-gateway/item/160-dlos8.html)  
4\. Real Time Environmental Monitoring in Palm Oil Plantation Using Wireless Sensor Network, accessed on December 14, 2024, [http://download.garuda.kemdikbud.go.id/article.php?article=549184\&val=7120\&title=Real%20Time%20Environmental%20Monitoring%20in%20Palm%20Oil%20Plantation%20Using%20Wireless%20Sensor%20Network](http://download.garuda.kemdikbud.go.id/article.php?article=549184&val=7120&title=Real+Time+Environmental+Monitoring+in+Palm+Oil+Plantation+Using+Wireless+Sensor+Network)  
5\. TrackerD \-- LoRaWAN Tracker User Manual \- Dragino Wiki, accessed on December 14, 2024, [https://wiki.dragino.com/xwiki/bin/view/Main/User%20Manual%20for%20LoRaWAN%20End%20Nodes/TrackerD/](https://wiki.dragino.com/xwiki/bin/view/Main/User%20Manual%20for%20LoRaWAN%20End%20Nodes/TrackerD/)  
6\. HKT GT-100 LoRaWAN® GPS Location Tracker (EU868) \- shopiot, accessed on December 14, 2024, [https://shopiot.eu/products/hkt-gt-100-lorawan%C2%AE-gps-location-tracker](https://shopiot.eu/products/hkt-gt-100-lorawan%C2%AE-gps-location-tracker)  
7\. Dragino LoRaWAN TrackerD mit BLE \+ GPS \- IoT-Shop, accessed on December 14, 2024, [https://iot-shop.de/en/shop/dg-trackerd-dragino-trackerd-lorawan-tracker-6063](https://iot-shop.de/en/shop/dg-trackerd-dragino-trackerd-lorawan-tracker-6063)  
8\. Milesight SG50 Ultra Low Power Solar LoRaWAN® Gateway, accessed on December 15, 2024, [https://www.milesight.com/company/blog/solar-power-lorawan-gateway](https://www.milesight.com/company/blog/solar-power-lorawan-gateway)  
9\. LoRa & LoRaWAN Temperature Humidity Sensor, accessed on December 14, 2024, [https://www.hktlora.com/product/lorawan-temperaturehumidity-sensor/](https://www.hktlora.com/product/lorawan-temperaturehumidity-sensor/)
