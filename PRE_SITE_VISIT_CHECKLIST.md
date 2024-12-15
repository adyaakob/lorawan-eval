# **Pre-Site Visit Checklist for LoRaWAN-based Worker Tracking System Evaluation**

**Report prepared for:** TEQ Armada Sdn Bhd

**Report prepared by:** Bard

**Date:** December 15, 2024

## **1. Introduction**

This report outlines the necessary preparations and verifications to be performed before conducting the on-site evaluation of the LoRaWAN-based worker tracking system in the selected oil palm estate. The objective is to ensure all necessary tools, equipment, and information are prepared and in working order for a smooth and efficient evaluation process.

## **2. Equipment and Tools**

Before the site visit, ensure the following equipment and tools are available and properly verified:

| Item | Model (Example) | Verification | Notes |
| :---- | :---- | :---- | :---- |
| Dragino Tracker D LoRaWAN GPS trackers | Dragino Tracker D | - Devices are fully charged. <br> - Device firmware is up-to-date. <br> - Device configurations (e.g., frequency band, data transmission interval) are set correctly. | Multiple trackers are recommended for comprehensive testing. |
| Dragino Outdoor Gateway DL0S86 (AS923) with 4G EC25 | Dragino DL0S86 | - Gateway is configured correctly (e.g., network server address, frequency band). <br> - 4G SIM card with sufficient data is installed and activated. <br> - Antenna is connected securely. |  |
| Laptop | Any suitable laptop | - Laptop is fully charged. <br> - LoRaWAN network server software (e.g., The Things Network, ChirpStack) is installed and configured. <br> - Mapping software (e.g., QGIS, Google Earth Pro) is installed. <br> - Necessary drivers and connectors are available. | **Note:** Contact the supplier of the chosen LoRaWAN network server software for recommendations on specific configurations and any available training resources 123. |
| High-accuracy GPS device | Garmin GPSMAP 66i | - Device is fully charged. <br> - Device settings (e.g., coordinate system, data logging) are configured correctly. | Alternatively, use a detailed map of the estate with sufficient accuracy. |
| Cellular signal strength meter | RF Explorer Handheld Spectrum Analyzer | - Device is calibrated and functioning correctly. <br> - Device is compatible with Malaysian cellular frequencies. | Alternatively, use a mobile phone with field test mode and a signal strength measurement app. See the list below for suitable options. |
| Measuring tape or laser distance measuring equipment | Bosch GLM 50 C | - Device is functioning correctly and batteries are installed. |  |
| Tools for mounting the gateway | Ladder, mounting brackets, tools | - Ensure you have the appropriate tools for the chosen mounting surface (e.g., wall, pole). |  |
| Power bank (optional) | Any suitable power bank | - Power bank is fully charged. | For charging devices in the field. |
| First-aid kit |  | - Kit is well-stocked with essential supplies. |  |

## **3. Software Verification**

Verify the functionality and compatibility of the following software:

* **LoRaWAN Network Server:** Ensure the network server is accessible and configured correctly. Test the connection with the Dragino DL0S86 gateway.  
* **Mapping Software:** Familiarize yourself with the mapping software and ensure you can import and visualize GPS data.  
* **Cellular Signal Strength Measurement:** If using a mobile phone, download and test a signal strength measurement app.

## **4. Site Information**

Gather the following information about the selected test site:

* **Estate Selection:** Choose the estate for testing and gather relevant information (e.g., maps, terrain details, potential obstacles).  
* **Contact Person:** Establish contact with a person on-site for access and assistance during the evaluation.  
* **Permissions:** Obtain any necessary permissions for accessing and installing equipment on the estate.

## **5. Safety Briefing**

Conduct a safety briefing with the evaluation team to discuss potential hazards and safety procedures in the plantation environment.

## **6. Data Collection Preparation**

* Prepare data collection forms for each test, ensuring all necessary fields are included.  
* Familiarize yourself with the data recording procedures and ensure all team members understand their roles.

## **7. Contingency Planning**

* Have backup equipment and tools available in case of any malfunctions.  
* Develop a plan for dealing with unexpected weather conditions or other potential disruptions.

## **8. Mobile Phones with Field Test Mode and Signal Strength Measurement Apps**

Here's a list of mobile phones and apps that can be used for measuring cellular signal strength:

**For iPhones:**

* **Field Test Mode:** Access by dialing \*3001\#12345\#\*  
  * Note that not all iPhones provide RSRP measurements due to carrier and chipset compatibility.  
* **Apps:**  
  * **weBoost App:** Provides a signal meter and field test mode instructions.  
  * **OpenSignal:** A reliable speed test tool with coverage maps.

**For Android:**

* **Field Test Mode:** Access varies by phone model and OS version, usually found under Settings.  
* **Apps:**  
  * **Network Cell Info Lite:** Provides a signal meter, network information, and cell tower locations.  
  * **SignalStream:** Shows field test information and allows sharing readings with signal specialists 4.

## **9. Conclusion**

By diligently completing this checklist, the evaluation team can ensure a well-prepared and successful on-site evaluation of the LoRaWAN-based worker tracking system. This will contribute to a comprehensive understanding of the system's feasibility and performance in the oil palm plantation environment.

### **Works cited**

1. Academy for LoRaWAN, accessed on December 15, 2024, [https://learn.semtech.com/](https://learn.semtech.com/)  
2. RAK7289 LoRaWAN Network Server Guide - RAKwireless Documentation Center, accessed on December 15, 2024, [https://docs.rakwireless.com/product-categories/wisgate/rak7289/lorawan-network-server-guide](https://docs.rakwireless.com/product-categories/wisgate/rak7289/lorawan-network-server-guide)  
3. Course: How to Build & Deploy a Network Using the LoRaWAN® Protocol, accessed on December 15, 2024, [https://learn.semtech.com/course/view.php?id=17](https://learn.semtech.com/course/view.php?id=17)  
4. Field Test Mode For iPhones and Android - Waveform, accessed on December 15, 2024, [https://www.waveform.com/a/b/guides/field-test-guide](https://www.waveform.com/a/b/guides/field-test-guide)
