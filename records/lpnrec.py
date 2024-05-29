from langchain_community.chat_models import ChatOllama
from langchain_core.messages import HumanMessage
from langchain_core.output_parsers import StrOutputParser
import base64
from io import BytesIO
from PIL import Image


class LicensePlateRecognition:
    def __init__(self, image_file):
        self.image_file = image_file
        self.pil_image = Image.open(self.image_file)
        self.llm = ChatOllama(model="llava", temperature=0)

    def convert_to_base64(self):
        buffered = BytesIO()
        self.pil_image.save(buffered, format="JPEG")
        img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
        return img_str

    def prompt_func(self, data):
        text = data["text"]
        image = data["image"]

        image_part = {
            "type": "image_url",
            "image_url": f"data:image/jpeg;base64,{image}",
        }

        content_parts = []

        text_part = {"type": "text", "text": text}

        content_parts.append(image_part)
        content_parts.append(text_part)

        return [HumanMessage(content=content_parts)]

    def recognize(self):
        image_b64 = self.convert_to_base64()
        chain = self.prompt_func | self.llm | StrOutputParser()

        return chain.invoke(
            {
                "text": "Give me the license plate number of this image",
                "image": image_b64,
            }
        )
