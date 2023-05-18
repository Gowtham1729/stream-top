# Stream-Top

Stream-Top is a learning project primarily focused on understanding and utilizing Apache Kafka through a real-world mini project. The idea for this project was inspired by educative.io's projects. It serves as a real-time system resource monitoring tool that uses Apache Kafka for data streaming, with the current capability to monitor CPU usage.

## Project Purpose and Scope

This project is intended for learning purposes, specifically for gaining a practical understanding of Apache Kafka. While the current iteration of the project supports CPU usage monitoring, there is potential to expand into other system resources in the future as part of the learning process.

By trying this project, you can gain hands-on experience with few of the important technologies and concepts such as Apache Kafka, Docker, Python, Plotly Dash, and Jupyter Notebooks. This project offers a tangible use-case to apply these technologies, making the learning process more engaging and effective.

## Getting Started

Follow the steps below to set up the project for development and testing:

### Prerequisites

Ensure you have the following installed on your local machine:

- Docker
- Python 3

### Installing

1. Clone the repository to your local machine.

```bash
git clone https://github.com/Gowtham1729/stream-top.git
cd stream-top
```

2. Start the Kafka broker and create the Kafka topic.

```bash
docker compose up -d
docker exec broker kafka-topics --bootstrap-server broker:9092 --create --topic top-events
```

3. Install Python dependencies.

```bash
pip install -r requirements.txt
```

4. Start the producer which will start sending CPU usage information to the Kafka topic.

```bash
python producer.py
```

5. Open the `consumer.ipynb` notebook in Jupyter and run it to start receiving and visualizing the CPU usage data.

## Usage

Stream-Top can be used to monitor the CPU usage of each core in real-time. The producer can be run on any machine to send CPU usage data to the Kafka topic, and the consumer notebook can be run anywhere with access to the Kafka topic to visualize the data.

## Future Scope

As part of the learning journey, future enhancements may include expanding the monitoring capabilities to other system resources such as memory usage, disk I/O, network traffic, etc.

## Acknowledgments

This project idea was inspired by the projects on educative.io. Special thanks to:

- The `psutil` library for providing system information
- Apache Kafka for data streaming capabilities
- Plotly Dash for visualization support
