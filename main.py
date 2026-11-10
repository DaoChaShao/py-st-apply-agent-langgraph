#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/11/10 17:27
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   main.py
# @Desc     :

from agents import (
    JobParser,
    ModelCategories,
    ModelOutputMethods,
    load_yaml,
)


def main() -> None:
    """ Main Function """
    job_description: str = """
    The Opportunity
    AUT is seeking a strategic and collaborative Enterprise Information Management Lead to take a pivotal role in shaping the University’s approach to data and information governance. This is a unique opportunity for a seasoned professional to drive operational leadership in managing AUT’s enterprise information assets, with a strong focus on unstructured data across file services and Microsoft 365 environments.
    Reporting to the Director, Data, Technology Risk & Policy, you will work across business and technology teams to embed governance, compliance, and lifecycle management practices that enable responsible and efficient use of information. As AUT continues to evolve its digital and data-driven capabilities, your leadership will be crucial in supporting data integrity, accessibility, and strategic value creation.
    This role offers the chance to contribute meaningfully to a forward-thinking academic institution, helping to create a data ecosystem that supports research, learning, and administration at all levels. You’ll be instrumental in enhancing information stewardship and ensuring alignment with both regulatory requirements and AUT’s long-term digital transformation goals.

    Key Responsibilities
    Provide operational leadership across AUT’s data estate
    Increase AUT’s information management maturity
    Help the University get more value from its data
    """

    seeker: str = load_yaml("configs.yaml", display=False)["deepseek"]
    opener: str = load_yaml("configs.yaml", display=False)["openai"]

    with JobParser(seeker, model_category=ModelCategories.DEEPSEEK, method=ModelOutputMethods.JSON_SCHEMA) as parser:
        result = parser.parse(job_description)
        print(result)

    with JobParser(opener, model_category=ModelCategories.OPENAI, method=ModelOutputMethods.JSON_SCHEMA) as parser:
        result = parser.parse(job_description)
        print(result)


if __name__ == "__main__":
    main()
