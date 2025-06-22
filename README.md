# 💌 Bop Common

**Bop Common** is the shared module for **Bop**, a work-in-progress Raspberry Pi-powered robot pet project.

Bop common isn't designed to run as a standalone app - It provides access to classes that are common between the codebases, such as DTO's, Enums and Exceptions.

This is **one of four core repositories**:
- [bop_sense](https://github.com/shane-chris-barker/bop_sense) - Listens to the world (mic, camera, sensors) and places AMQP or MQTT messages into a queue.

- [bop_brain](https://github.com/shane-chris-barker/bop_brain) - Responsible for processing the messages produced by `bop_sense` and making decisions based on their content.

- `bop_body` - Does not exist yet but will subscribe and readt to commands produced by `bop_brain` and then take an action (motors, display, feedback etc)

> ⚠️ **Note**: This is an early, rough WIP and very much an experiment. Things will change, break, and improve rapidly. 

>I'm also very new to Python, so there are bound to be mistakes...

---

## 🧪 Testing

Tests are available using Pytest

```bash
pytest
```


