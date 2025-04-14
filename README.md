# School Management System API

This project is a **School Management System** based on an API, aimed at facilitating communication and managing information between teachers and students. The system is implemented using **Django** and **Django REST Framework** and provides various features for interaction between users.

## Features

### 1. **School and User Management**
   - The system admin can manage schools, teachers, and students. The admin can create new schools, view user information, and approve or reject registration requests.

### 2. **News and Assignments Management**
   - Teachers can create news and assignments, send assignments with deadlines and various attachments (PDF or ZIP), and record the last modification dates.

### 3. **Teacher-Student Chat**
   - The internal chat system allows teachers and students to easily communicate by sending and receiving messages.

### 4. **Geographic Information System (GIS)**
   - Using geographic data, users can view the nearest schools based on their location. Additionally, geographic information for schools and students is stored.

### 5. **Secure Login and Registration**
   - Users can log in using their username and password. Teachers and students can also update their profile information.
   - The system is designed so that teachers can teach multiple subjects in different schools, and students only have access to news and assignments related to them. It also allows tracking news views and sharing courses.

## Purpose
The main goal of this project is to provide a secure and efficient platform for managing schools and communication between teachers and students. By implementing this system, teachers can easily publish news and assignments, and students can respond to assignments and stay updated with news.

## GIS Integration
This project utilizes GIS features to manage the geographic locations of schools and students, allowing users to view nearby schools based on their location.

## Chat System
The chat system is a simple communication tool for sending and receiving messages between teachers and students, improving interaction and faster response to queries.

## Unit Tests
All APIs in the project are evaluated using unit tests to ensure that all functionalities work correctly and that potential issues are identified and fixed.

## Conclusion
This project helps administrators, teachers, and students communicate effectively and manage educational and administrative processes efficiently.
