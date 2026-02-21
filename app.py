import json
import streamlit as st
from streamlit.components.v1 import html

# Mermaid diagram: Updated with Bidirectional Feedback Loops, Grid Constraints, and Advanced Packaging
MERMAID_DIAGRAM = """
graph LR
    %% =====================
    %% STYLING DEFINITIONS
    %% =====================
    classDef china fill:#fee2e2,stroke:#ef4444,stroke-width:2px;
    classDef us fill:#dbeafe,stroke:#3b82f6,stroke-width:2px;
    classDef nl fill:#f0fdf4,stroke:#22c55e,stroke-width:2px;
    classDef tw fill:#faf5ff,stroke:#a855f7,stroke-width:2px;
    classDef jp fill:#fef3c7,stroke:#f59e0b,stroke-width:2px;
    classDef infra fill:#f3f4f6,stroke:#374151,stroke-width:2px;
    classDef capital fill:#ecfeff,stroke:#0891b2,stroke-width:2px;
    classDef architect fill:#e8f5e9,stroke:#2e7d32,stroke-width:3px;
    classDef feedback fill:#fff3e0,stroke:#2e7d32,stroke-dasharray: 5 5,stroke-width:2px;

    %% THE RED ECONOMIC VALUE CLASS
    classDef money fill:#ffebee,stroke:#d50000,stroke-width:3px,color:#d50000,font-weight:bold;

    %% =====================
    %% LAYER 6 - THE AGENTIC INTERFACE (YOU)
    %% =====================
    subgraph L6["6. The Agentic Interface (Value Capture)"]
        direction TB
        Input[Task Input]
        Gate{The Gate:<br/>Routine?}:::architect
        Agents["🤖 AI Agents<br/>Compute Consumer"]:::architect
        You["👷 The Architect<br/>Strategy & QA"]:::architect

        %% ECONOMIC VALUE
        Val6["$15.7T Global GDP Impact<br/>(2030 PwC Est)"]:::money

        Input --> Gate
        Gate -->|Yes| Agents
        Gate -->|No| You
        Agents --> You
        You -.-> Val6
    end

    %% =====================
    %% LAYER 5 - CAPITAL STACK
    %% =====================
    subgraph L5["5. Capital Stack"]
        Goldman["Goldman Sachs<br/>Capital Solutions"]:::us
        VC["Private Credit<br/>GIC - CPP - Blue Owl"]:::capital

        %% ECONOMIC VALUE
        Val5["~$3T+ Liquid Capital<br/>(Dry Powder seeking Yield)"]:::money

        Goldman -.-> Val5
        VC -.-> Val5
    end

    %% =====================
    %% LAYER 4 - COMPUTE AND POWER BOTTLENECK
    %% =====================
    subgraph L4["4. Compute and Power Bottleneck"]
        Grid["Transmission Grid & Transformers<br/>5-10 Year Backlog"]:::infra
        Hyperscalers["Hyperscalers<br/>AWS - Google - Meta - Azure"]:::us
        Workload["AI Workload Shifting<br/>Spatial & Temporal"]:::us
        Stargate["Project Stargate<br/>$100B-$500B JV"]
        Power["Baseload Power<br/>Nuclear - Grid"]:::infra
        Cooling["Thermal & Water Systems<br/>1200B Liters by 2030"]:::infra

        %% ECONOMIC VALUE
        Val4["~$8T Combined Mkt Cap<br/>(The Cloud Oligopoly)"]:::money
        Val4b["$1T AI CapEx Spending<br/>(Infrastructure Investment)"]:::money

        Hyperscalers -.-> Val4
        Stargate -.-> Val4b
    end

    %% =====================
    %% LAYER 3 - FABRICATION
    %% =====================
    subgraph L3["3. Fabrication"]
        TSMC["TSMC Foundry<br/>~60% Advanced Share"]:::tw
        Samsung["Samsung Foundry"]:::tw
        Packaging["Advanced Packaging<br/>CoWoS & HBM"]:::tw

        %% ECONOMIC VALUE
        Val3["~$900B Mkt Cap<br/>(Manufacturing Monopoly)"]:::money

        TSMC -.-> Val3
    end

    %% =====================
    %% LAYER 2 - DESIGN AND CRITICAL TOOLS
    %% =====================
    subgraph L2["2. Design and Critical Tools"]
        EDA["EDA Software<br/>Synopsys - Cadence"]:::us
        ASML["EUV Lithography<br/>ASML Monopoly"]:::nl
        Design["AI Chip Design<br/>NVIDIA - AMD - Huawei"]:::us

        %% ECONOMIC VALUE
        Val2a["~$350B Mkt Cap<br/>(The Machine Maker)"]:::money
        Val2b["~$3.5T Mkt Cap<br/>(The Design Premium)"]:::money

        ASML -.-> Val2a
        Design -.-> Val2b
    end

    %% =====================
    %% LAYER 1 - RAW MATERIALS
    %% =====================
    subgraph L1["1. Raw Materials"]
        REE["Rare Earths & Gallium<br/>Nd - Y - Ga"]:::china
        ChinaGov["China Mining and Refining<br/>~90% Global Monopoly"]:::china

        %% ECONOMIC VALUE
        Val1["~$15B Market Size<br/>(Strategic Choke Point)"]:::money

        ChinaGov -.-> Val1
    end

    %% =====================
    %% CORE LINEAR FLOW CONNECTIONS
    %% =====================
    REE --> ChinaGov
    ChinaGov --> Grid
    EDA --> Design
    ASML --> TSMC
    Design --> TSMC
    TSMC --> Packaging
    Packaging --> Hyperscalers

    %% =====================
    %% THE POWER & COMPUTE NEXUS
    %% =====================
    Power --> Grid
    Grid --> Hyperscalers
    Grid --> Cooling
    Hyperscalers <--> Workload
    Workload <--> Grid

    %% CAPITAL INJECTION (Fueling the Bottleneck)
    Goldman ==> Stargate
    VC ==> Hyperscalers
    Stargate ==> Power

    %% COMPUTE TO ARCHITECT (The Critical Link)
    Hyperscalers ==> Agents

    %% =====================
    %% THE AI FEEDBACK LOOP (BIDIRECTIONAL LOGIC)
    %% =====================
    Agents -. "AI for Grid Optimization<br/>(Unlocks 175GW)" .-> Grid
    Agents -. "AI Material Discovery<br/>(Self-Driving Labs)" .-> L1
"""

# Expanded intelligence layers with high-depth analysis of chokepoints and citations
LAYER_MARKDOWN = {
    "AI Supply Chain: Overview": """
The AI supply chain is undergoing a fundamental transformation, shifting from a focus on software code to a massive, resource-intensive industrial marathon. This explorer identifies the critical chokepoints where technical, geopolitical, and environmental constraints collide.

The primary systemic challenge is the clash of timescales. While AI models iterate and double in complexity every few months, the physical infrastructure they require—foundries, reactors, and transmission lines—takes years to deploy. This mismatch is why compute progress is now gated by "land and steel" rather than just "math and logic." 

**The AI Feedback Loop:** The supply chain is no longer linear. While AI consumes massive resources, it is also becoming the primary tool to optimize them. For instance, AI applications can unlock up to 175 GW of hidden capacity in existing transmission lines without building new ones. AI is also compressing the time needed to discover new battery chemistries and catalysts from decades down to months using self-driving laboratories.

The ultimate destination of this supply chain is the **Agentic Interface**. The trillions of dollars invested in Layers 1-5 exist to generate intelligence that must be converted into economic value by human architects. Estimates suggest AI could add **$15.7 trillion** to the global economy by 2030.
""",
    "Layer 1 - Resource and Extraction": """
### 1. The Resource and Extraction Phase (Layer 1)

**Layer Challenges:** The foundation of the AI era relies on geological scarcity. While elements like silicon are abundant, the Rare Earth Elements (REEs) required for high-performance hardware exist in low concentrations and are notoriously difficult to separate and refine without severe environmental degradation.

**The Chinese Refining Monopoly:** China currently maintains a ~90% global monopoly over REE refining. Furthermore, data centers require vast amounts of Gallium for high-frequency power converters. Data center demand for gallium could equal up to 11% of today’s supply by 2030, a critical risk considering China accounts for 98% of gallium refining.

**The Purity Standard:** Quartz sand must be purified to 9N (99.9999999%) to become semiconductor-grade silicon. Through the Czochralski method, single-crystal silicon ingots are grown and sliced into thin wafers. Any microscopic impurity at this stage can cause faults that render a multi-billion transistor chip completely non-functional.
""",
    "Layer 2 - Design and Tooling": """
### 2. The Design and Tooling Moat (Layer 2)

**Layer Challenges:** This layer represents the knowledge moat. The software and machinery required to build modern AI chips are the result of decades of cumulative industrial experience that cannot be replicated through simple capital investment.

**EDA Gatekeepers:** American firms like Synopsys and Cadence dominate roughly 80% of the Electronic Design Automation (EDA) market in China, serving as the ultimate software gatekeepers. Without EDA, advanced architectural concepts like FinFET or GAAFET (Gate-All-Around) cannot be physically realized on silicon.

**The EUV Chokepoint:** The Netherlands' ASML is the solo global provider of Extreme Ultraviolet (EUV) lithography. These machines took billions of dollars and three decades to develop. This technology is mandatory for producing chips at 5nm and below, making it the primary target for international export controls.
""",
    "Layer 3 - Fabrication": """
### 3. The Fabrication and Packaging Loop (Layer 3)

**Layer Challenges:** Fabrication is geographically concentrated and extremely high-risk. A single fab takes about three years, $10B, and 6,000 construction workers to build.

**Taiwan-Centricity:** TSMC (Taiwan) is the absolute market leader, dominating around 60% of the advanced foundry market share. This geographic concentration creates a single point of failure for the global digital economy.

**The Advanced Packaging Bottleneck:** The bottleneck has moved from making chips to stacking them. Advanced packaging techniques like CoWoS (Chip-on-Wafer-on-Substrate) are used to microscopicly fuse logic GPUs with High-Bandwidth Memory (HBM) chiplets. While China has a 14% global market share in general assembly and test, advanced packaging like CoWoS remains heavily dominated by Taiwanese firms.
""",
    "Layer 4 - Power and Infrastructure": """
### 4. The Power, Grid, and Infrastructure Bottleneck (Layer 4)

**Layer Challenges:** AI compute demand is advancing at digital speed, but the energy system requires long lead times to schedule and build infrastructure. Data centers could consume 945 TWh by 2030, effectively doubling current energy draw.

**The Transmission Bottleneck:** Building a new data center takes 1-3 years, but building new transmission lines can take four to eight years. Order backlogs for power transformers grew by more than 30% in 2024, and grid connection queues for new data centers can now take up to 10 years in places like the Netherlands. Around one-fifth of global data center capacity additions could be delayed due to grid constraints.

**Workload Shifting:** To mitigate grid saturation, AI models can utilize temporal and spatial workload shifting. Because AI training is latency-tolerant, workloads can be shifted across data centers to times and locations where renewable energy is abundant and grid congestion is low.

**The Water Constraint:** AI's thirst is literal. Global water consumption for data centers is projected to reach 1,200 billion liters by 2030. Notably, 60% of this water footprint is indirect, stemming from power generation cooling and the ultra-pure water required for semiconductor manufacturing.
""",
    "Layer 5 - Capital Stack": """
### 5. Financial Engineering and Capital Stack (Layer 5)

**Layer Challenges:** AI infrastructure represents a new asset class that traditional banking is not yet fully equipped to handle. The massive average cost of a single 250 MW data center unit is roughly $12B inclusive of the equipment inside.

**The Obsolescence Mismatch:** The compute equipment inside AI data centers costs 3-4x more than the physical data center itself, and the rapid pace of innovation creates uncertainty around hardware relevance.

**Capital Recycling:** Investment banks like Goldman Sachs create liquidity by refinancing stabilized, cash-flowing data centers into Asset-Backed Securities (ABS). This allows developers to pull their equity out of completed projects and recycle it into the next wave of infrastructure, sustaining the CapEx cycle.
""",
    "Layer 6 - The Agentic Interface": """
### 6. The Agentic Interface and Value Capture (Layer 6)

**Layer Challenges:** This is the "Last Mile" problem. The massive compute power generated in Layers 1-5 is useless if it is bottlenecked by human manual execution. The challenge is shifting the workforce from "Doing" to "Designing."

**The Architect vs. The Hero:** The "Hero" operator, who manually processes data and code, is a scalability bottleneck. The new economic unit is the "Architect," who uses a "Gate" mechanism to filter routine tasks to AI Agents. This shift allows a single individual to orchestrate the output of hundreds of digital workers.

**The Bidirectional Feedback Loop:** While Layers 1-5 represent **Cost** (CapEx and Opex), Layer 6 represents **Revenue** and **Innovation**. AI is feeding back into the supply chain to solve its own bottlenecks. AI models are being used to map protein structures in days instead of years, discover new catalyst materials, and dynamically route power across transmission grids.

**The 15.7 Trillion Opportunity:** It is estimated that AI could add $15.7 trillion to the global economy by 2030. This value is ultimately captured by the businesses and individuals who successfully deploy these agents.
""",
    "Sources and References": """
### Primary Sources for this Analysis

- **Institute for AI Policy and Strategy (IAPS):**  
  *Introduction to AI Chip Making in China (Dec 2023)*  
  Details on EUV lithography, EDA software choke points, advanced CoWoS packaging, and foreign direct product rule (FDPR) export controls.

- **Goldman Sachs:**  
  *Powering the AI Era (Global Investment Banking)*  
  Sourcing for the $12B data center cost metric, asset-backed securities (ABS) capital recycling, and hyperscaler joint ventures.

- **International Energy Agency (IEA):**  
  *Energy and AI (World Energy Outlook Special Report)*  
  Source for the bidirectional AI feedback loop (AI unlocking grid capacity, self-driving labs), the 5-10 year transformer backlog, the 1,200 billion liter water constraint, and data center grid connection delays.

- **Kinaxis:**  
  *The Supply Chain of AI (Faye Baker)*  
  Source for China's 90% REE refining monopoly, silicon purity standards, and the $15.7 trillion global GDP projection.
z
"""
}

NODE_TO_LAYER = {
    "REE": "Layer 1 - Resource and Extraction",
    "ChinaGov": "Layer 1 - Resource and Extraction",
    "EDA": "Layer 2 - Design and Tooling",
    "ASML": "Layer 2 - Design and Tooling",
    "Design": "Layer 2 - Design and Tooling",
    "TSMC": "Layer 3 - Fabrication",
    "Samsung": "Layer 3 - Fabrication",
    "Packaging": "Layer 3 - Fabrication",
    "Grid": "Layer 4 - Power and Infrastructure",
    "Workload": "Layer 4 - Power and Infrastructure",
    "Hyperscalers": "Layer 4 - Power and Infrastructure",
    "Stargate": "Layer 4 - Power and Infrastructure",
    "Power": "Layer 4 - Power and Infrastructure",
    "Cooling": "Layer 4 - Power and Infrastructure",
    "Goldman": "Layer 5 - Capital Stack",
    "VC": "Layer 5 - Capital Stack",
    "Input": "Layer 6 - The Agentic Interface",
    "Gate": "Layer 6 - The Agentic Interface",
    "Agents": "Layer 6 - The Agentic Interface",
    "You": "Layer 6 - The Agentic Interface",
}


def render_mermaid(diagram: str, height: int = 800) -> None:
    node_map = json.dumps(NODE_TO_LAYER)
    html(
        f"""
        <style>
            #mermaid-container {{ width: 100%; height: 520px; background: #ffffff; border-radius: 12px; border: 1px solid #e2e8f0; overflow: hidden; display: flex; align-items: center; justify-content: center; }}
            .mermaid {{ width: 100%; height: 100%; }}
        </style>
        <div id="mermaid-container"><div class="mermaid" id="graph-div">{diagram}</div></div>
        <script src="https://cdn.jsdelivr.net/npm/svg-pan-zoom@3.6.1/dist/svg-pan-zoom.min.js"></script>
        <script type="module">
            import mermaid from "https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs";
            mermaid.initialize({{ startOnLoad: false, theme: "neutral", securityLevel: 'loose', flowchart: {{ useMaxWidth: false, htmlLabels: true, curve: 'basis' }} }});
            async function render() {{
                const element = document.querySelector("#graph-div");
                const {{ svg }} = await mermaid.render('rendered-svg', element.textContent);
                element.innerHTML = svg;
                const svgElement = document.querySelector("#rendered-svg");
                if (svgElement) {{
                    svgElement.style.width = "100%"; svgElement.style.height = "100%";
                    svgPanZoom(svgElement, {{ zoomEnabled: true, panEnabled: true, controlIconsEnabled: true, fit: true, center: true, minZoom: 0.1, maxZoom: 10 }});
                }}
            }}
            render();
        </script>
        """,
        height=height,
    )


def main() -> None:
    st.set_page_config(page_title="AI Supply Chain Explorer", layout="wide")

    # --- HEADER ---
    # Uchicago shield image (local file)
    uchicago_shield_url = "UChicago_Shield_1Color_Maroon_RGB.png"
    with st.container():
        col_logo, col_title = st.columns([1, 7])
        with col_logo:
            st.image(uchicago_shield_url, width=60)
        with col_title:
            st.title("AI Supply Chain Explorer")
            st.caption(
                "Mapping the global AI hardware, power, and capital ecosystem.")

    st.markdown(
        "<style>div.block-container{padding-top:1.5rem;}</style>", unsafe_allow_html=True)

    # --- SIDEBAR ---
    st.sidebar.image(uchicago_shield_url, width=50)
    st.sidebar.title("Layer Intelligence")
    layer_options = [
        "AI Supply Chain: Overview",
        "Layer 1 - Resource and Extraction",
        "Layer 2 - Design and Tooling",
        "Layer 3 - Fabrication",
        "Layer 4 - Power and Infrastructure",
        "Layer 5 - Capital Stack",
        "Layer 6 - The Agentic Interface",
        "Sources and References"
    ]
    if "selected_layer" not in st.session_state:
        st.session_state.selected_layer = layer_options[0]
    selected_layer = st.sidebar.radio(
        "Select a Layer to Investigate:",
        options=layer_options,
        key="layer_nav_radio",
    )
    st.sidebar.markdown("---")
    st.sidebar.markdown(LAYER_MARKDOWN[selected_layer])
    st.sidebar.markdown("---")
    st.sidebar.info("Contact: ai-team@example.com")

    # --- MAIN CONTENT ---
    with st.container():
        st.subheader("System Interaction Map")
        st.markdown(
            "Visualize the flow of resources, capital, and intelligence across the AI supply chain."
        )
        render_mermaid(MERMAID_DIAGRAM)
        st.caption(
            "Use the sidebar to select an intelligence layer for deep-dive analysis and source references."
        )

    st.markdown("---")

    # --- METRICS ---
    with st.container():
        st.subheader("Key Market Metrics (Data-Validated)")
        m1, m2, m3 = st.columns(3)
        m1.metric("🌎 Global Economic Impact (2030)", "$15.7 Trillion")
        m2.metric("💸 Projected AI CapEx (2027)", "$1.0 Trillion")
        m3.metric("🇨🇳 China REE Mono-Refining", "90%")

    # --- FOOTER ---
    st.markdown("---")
    st.markdown(
        "<div style='text-align: center; color: gray;'>© 2026 AI Supply Chain Explorer | v1.0</div>",
        unsafe_allow_html=True,
    )


if __name__ == "__main__":
    main()
