"""
型定義を提供するモジュール
"""

from dataclasses import dataclass
from typing import TypedDict


@dataclass
class Result:
    url: str
    title_translated: str
    title_original: str
    words: list[str]
    subjects: list[str]


# see https://note.nkmk.me/python-arxiv-api-download-rss/


class Article(TypedDict):
    arxiv_url: str
    title: str
    summary: str
    tags: list[dict[str, str]]


class Config(TypedDict):
    subject: str
    keywords: list[str]


# script/get_taxonomy.py で取得したもの
taxonomy: dict[str, dict[str, str]] = {
    "cs.AI": {
        "category": "cs.AI",
        "name": "Artificial Intelligence",
        "description": "Covers all areas of AI except Vision, Robotics, Machine Learning, Multiagent Systems, and Computation and Language (Natural Language Processing), which have separate subject areas. In particular, includes Expert Systems, Theorem Proving (although this may overlap with Logic in Computer Science), Knowledge Representation, Planning, and Uncertainty in AI. Roughly includes material in ACM Subject Classes I.2.0, I.2.1, I.2.3, I.2.4, I.2.8, and I.2.11.",
    },
    "cs.AR": {
        "category": "cs.AR",
        "name": "Hardware Architecture",
        "description": "Covers systems organization and hardware architecture. Roughly includes material in ACM Subject Classes C.0, C.1, and C.5.",
    },
    "cs.CC": {
        "category": "cs.CC",
        "name": "Computational Complexity",
        "description": "Covers models of computation, complexity classes, structural complexity, complexity tradeoffs, upper and lower bounds. Roughly includes material in ACM Subject Classes F.1 (computation by abstract devices), F.2.3 (tradeoffs among complexity measures), and F.4.3 (formal languages), although some material in formal languages may be more appropriate for Logic in Computer Science. Some material in F.2.1 and F.2.2, may also be appropriate here, but is more likely to have Data Structures and Algorithms as the primary subject area.",
    },
    "cs.CE": {
        "category": "cs.CE",
        "name": "Computational Engineering, Finance, and Science",
        "description": "Covers applications of computer science to the mathematical modeling of complex systems in the fields of science, engineering, and finance. Papers here are interdisciplinary and applications-oriented, focusing on techniques and tools that enable challenging computational simulations to be performed, for which the use of supercomputers or distributed computing platforms is often required. Includes material in ACM Subject Classes J.2, J.3, and J.4 (economics).",
    },
    "cs.CG": {
        "category": "cs.CG",
        "name": "Computational Geometry",
        "description": "Roughly includes material in ACM Subject Classes I.3.5 and F.2.2.",
    },
    "cs.CL": {
        "category": "cs.CL",
        "name": "Computation and Language",
        "description": "Covers natural language processing. Roughly includes material in ACM Subject Class I.2.7. Note that work on artificial languages (programming languages, logics, formal systems) that does not explicitly address natural-language issues broadly construed (natural-language processing, computational linguistics, speech, text retrieval, etc.) is not appropriate for this area.",
    },
    "cs.CR": {
        "category": "cs.CR",
        "name": "Cryptography and Security",
        "description": "Covers all areas of cryptography and security including authentication, public key cryptosytems, proof-carrying code, etc. Roughly includes material in ACM Subject Classes D.4.6 and E.3.",
    },
    "cs.CV": {
        "category": "cs.CV",
        "name": "Computer Vision and Pattern Recognition",
        "description": "Covers image processing, computer vision, pattern recognition, and scene understanding. Roughly includes material in ACM Subject Classes I.2.10, I.4, and I.5.",
    },
    "cs.CY": {
        "category": "cs.CY",
        "name": "Computers and Society",
        "description": "Covers impact of computers on society, computer ethics, information technology and public policy, legal aspects of computing, computers and education. Roughly includes material in ACM Subject Classes K.0, K.2, K.3, K.4, K.5, and K.7.",
    },
    "cs.DB": {
        "category": "cs.DB",
        "name": "Databases",
        "description": "Covers database management, datamining, and data processing. Roughly includes material in ACM Subject Classes E.2, E.5, H.0, H.2, and J.1.",
    },
    "cs.DC": {
        "category": "cs.DC",
        "name": "Distributed, Parallel, and Cluster Computing",
        "description": "Covers fault-tolerance, distributed algorithms, stabilility, parallel computation, and cluster computing. Roughly includes material in ACM Subject Classes C.1.2, C.1.4, C.2.4, D.1.3, D.4.5, D.4.7, E.1.",
    },
    "cs.DL": {
        "category": "cs.DL",
        "name": "Digital Libraries",
        "description": "Covers all aspects of the digital library design and document and text creation. Note that there will be some overlap with Information Retrieval (which is a separate subject area). Roughly includes material in ACM Subject Classes H.3.5, H.3.6, H.3.7, I.7.",
    },
    "cs.DM": {
        "category": "cs.DM",
        "name": "Discrete Mathematics",
        "description": "Covers combinatorics, graph theory, applications of probability. Roughly includes material in ACM Subject Classes G.2 and G.3.",
    },
    "cs.DS": {
        "category": "cs.DS",
        "name": "Data Structures and Algorithms",
        "description": "Covers data structures and analysis of algorithms. Roughly includes material in ACM Subject Classes E.1, E.2, F.2.1, and F.2.2.",
    },
    "cs.ET": {
        "category": "cs.ET",
        "name": "Emerging Technologies",
        "description": "Covers approaches to information processing (computing, communication, sensing) and bio-chemical analysis based on alternatives to silicon CMOS-based technologies, such as nanoscale electronic, photonic, spin-based, superconducting, mechanical, bio-chemical and quantum technologies (this list is not exclusive). Topics of interest include (1) building blocks for emerging technologies, their scalability and adoption in larger systems, including integration with traditional technologies, (2) modeling, design and optimization of novel devices and systems, (3) models of computation, algorithm design and programming for emerging technologies.",
    },
    "cs.FL": {
        "category": "cs.FL",
        "name": "Formal Languages and Automata Theory",
        "description": "Covers automata theory, formal language theory, grammars, and combinatorics on words. This roughly corresponds to ACM Subject Classes F.1.1, and F.4.3. Papers dealing with computational complexity should go to cs.CC; papers dealing with logic should go to cs.LO.",
    },
    "cs.GL": {
        "category": "cs.GL",
        "name": "General Literature",
        "description": "Covers introductory material, survey material, predictions of future trends, biographies, and miscellaneous computer-science related material. Roughly includes all of ACM Subject Class A, except it does not include conference proceedings (which will be listed in the appropriate subject area).",
    },
    "cs.GR": {
        "category": "cs.GR",
        "name": "Graphics",
        "description": "Covers all aspects of computer graphics. Roughly includes material in all of ACM Subject Class I.3, except that I.3.5 is is likely to have Computational Geometry as the primary subject area.",
    },
    "cs.GT": {
        "category": "cs.GT",
        "name": "Computer Science and Game Theory",
        "description": "Covers all theoretical and applied aspects at the intersection of computer science and game theory, including work in mechanism design, learning in games (which may overlap with Learning), foundations of agent modeling in games (which may overlap with Multiagent systems), coordination, specification and formal methods for non-cooperative computational environments. The area also deals with applications of game theory to areas such as electronic commerce.",
    },
    "cs.HC": {
        "category": "cs.HC",
        "name": "Human-Computer Interaction",
        "description": "Covers human factors, user interfaces, and collaborative computing. Roughly includes material in ACM Subject Classes H.1.2 and all of H.5, except for H.5.1, which is more likely to have Multimedia as the primary subject area.",
    },
    "cs.IR": {
        "category": "cs.IR",
        "name": "Information Retrieval",
        "description": "Covers indexing, dictionaries, retrieval, content and analysis. Roughly includes material in ACM Subject Classes H.3.0, H.3.1, H.3.2, H.3.3, and H.3.4.",
    },
    "cs.IT": {
        "category": "cs.IT",
        "name": "Information Theory",
        "description": "Covers theoretical and experimental aspects of information theory and coding. Includes material in ACM Subject Class E.4 and intersects with H.1.1.",
    },
    "cs.LG": {
        "category": "cs.LG",
        "name": "Machine Learning",
        "description": "Papers on all aspects of machine learning research (supervised, unsupervised, reinforcement learning, bandit problems, and so on) including also robustness, explanation, fairness, and methodology. cs.LG is also an appropriate primary category for applications of machine learning methods.",
    },
    "cs.LO": {
        "category": "cs.LO",
        "name": "Logic in Computer Science",
        "description": "Covers all aspects of logic in computer science, including finite model theory, logics of programs, modal logic, and program verification. Programming language semantics should have Programming Languages as the primary subject area. Roughly includes material in ACM Subject Classes D.2.4, F.3.1, F.4.0, F.4.1, and F.4.2; some material in F.4.3 (formal languages) may also be appropriate here, although Computational Complexity is typically the more appropriate subject area.",
    },
    "cs.MA": {
        "category": "cs.MA",
        "name": "Multiagent Systems",
        "description": "Covers multiagent systems, distributed artificial intelligence, intelligent agents, coordinated interactions. and practical applications. Roughly covers ACM Subject Class I.2.11.",
    },
    "cs.MM": {
        "category": "cs.MM",
        "name": "Multimedia",
        "description": "Roughly includes material in ACM Subject Class H.5.1.",
    },
    "cs.MS": {
        "category": "cs.MS",
        "name": "Mathematical Software",
        "description": "Roughly includes material in ACM Subject Class G.4.",
    },
    "cs.NA": {
        "category": "cs.NA",
        "name": "Numerical Analysis",
        "description": "cs.NA is an alias for math.NA. Roughly includes material in ACM Subject Class G.1.",
    },
    "cs.NE": {
        "category": "cs.NE",
        "name": "Neural and Evolutionary Computing",
        "description": "Covers neural networks, connectionism, genetic algorithms, artificial life, adaptive behavior. Roughly includes some material in ACM Subject Class C.1.3, I.2.6, I.5.",
    },
    "cs.NI": {
        "category": "cs.NI",
        "name": "Networking and Internet Architecture",
        "description": "Covers all aspects of computer communication networks, including network architecture and design, network protocols, and internetwork standards (like TCP/IP). Also includes topics, such as web caching, that are directly relevant to Internet architecture and performance. Roughly includes all of ACM Subject Class C.2 except C.2.4, which is more likely to have Distributed, Parallel, and Cluster Computing as the primary subject area.",
    },
    "cs.OH": {
        "category": "cs.OH",
        "name": "Other Computer Science",
        "description": "This is the classification to use for documents that do not fit anywhere else.",
    },
    "cs.OS": {
        "category": "cs.OS",
        "name": "Operating Systems",
        "description": "Roughly includes material in ACM Subject Classes D.4.1, D.4.2., D.4.3, D.4.4, D.4.5, D.4.7, and D.4.9.",
    },
    "cs.PF": {
        "category": "cs.PF",
        "name": "Performance",
        "description": "Covers performance measurement and evaluation, queueing, and simulation. Roughly includes material in ACM Subject Classes D.4.8 and K.6.2.",
    },
    "cs.PL": {
        "category": "cs.PL",
        "name": "Programming Languages",
        "description": "Covers programming language semantics, language features, programming approaches (such as object-oriented programming, functional programming, logic programming). Also includes material on compilers oriented towards programming languages; other material on compilers may be more appropriate in Architecture (AR). Roughly includes material in ACM Subject Classes D.1 and D.3.",
    },
    "cs.RO": {
        "category": "cs.RO",
        "name": "Robotics",
        "description": "Roughly includes material in ACM Subject Class I.2.9.",
    },
    "cs.SC": {
        "category": "cs.SC",
        "name": "Symbolic Computation",
        "description": "Roughly includes material in ACM Subject Class I.1.",
    },
    "cs.SD": {
        "category": "cs.SD",
        "name": "Sound",
        "description": "Covers all aspects of computing with sound, and sound as an information channel. Includes models of sound, analysis and synthesis, audio user interfaces, sonification of data, computer music, and sound signal processing. Includes ACM Subject Class H.5.5, and intersects with H.1.2, H.5.1, H.5.2, I.2.7, I.5.4, I.6.3, J.5, K.4.2.",
    },
    "cs.SE": {
        "category": "cs.SE",
        "name": "Software Engineering",
        "description": "Covers design tools, software metrics, testing and debugging, programming environments, etc. Roughly includes material in all of ACM Subject Classes D.2, except that D.2.4 (program verification) should probably have Logics in Computer Science as the primary subject area.",
    },
    "cs.SI": {
        "category": "cs.SI",
        "name": "Social and Information Networks",
        "description": "Covers the design, analysis, and modeling of social and information networks, including their applications for on-line information access, communication, and interaction, and their roles as datasets in the exploration of questions in these and other domains, including connections to the social and biological sciences. Analysis and modeling of such networks includes topics in ACM Subject classes F.2, G.2, G.3, H.2, and I.2; applications in computing include topics in H.3, H.4, and H.5; and applications at the interface of computing and other disciplines include topics in J.1--J.7. Papers on computer communication systems and network protocols (e.g. TCP/IP) are generally a closer fit to the Networking and Internet Architecture (cs.NI) category.",
    },
    "cs.SY": {
        "category": "cs.SY",
        "name": "Systems and Control",
        "description": "cs.SY is an alias for eess.SY. This section includes theoretical and experimental research covering all facets of automatic control systems. The section is focused on methods of control system analysis and design using tools of modeling, simulation and optimization. Specific areas of research include nonlinear, distributed, adaptive, stochastic and robust control in addition to hybrid and discrete event systems. Application areas include automotive and aerospace control systems, network control, biological systems, multiagent and cooperative control, robotics, reinforcement learning, sensor networks, control of cyber-physical and energy-related systems, and control of computing systems.",
    },
}
