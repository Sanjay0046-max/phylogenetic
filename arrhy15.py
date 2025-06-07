import streamlit as st
import pandas as pd
import os
from streamlit_option_menu import option_menu

st.markdown("""
    <style>
    /* 3D Heading Style */
    .three-d-heading {
        font-size: 48px;
        font-weight: bold;
        color: #ffffff;
        text-align: center;
        background: linear-gradient(to right, #1f1c2c, #928dab);
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.5);
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.6);
        margin-bottom: 25px;
    }

    /* Menu bar styling */
    .css-1d391kg {
        background: linear-gradient(to right, #232526, #414345);
        box-shadow: 0 3px 6px rgba(0,0,0,0.3);
        border-radius: 8px;
        padding: 8px;
    }

    table {
        font-size: 10px;
    }
    th {
        font-size: 10px;
    }
    td {
        font-size: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Load dataset
def load_data():
    try:
        file_path = r"arrhythmia database.xlsx"
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found at {file_path}")
        return pd.read_excel(file_path)
    except Exception as e:
        st.error(f"Error: {e}")
        return None

# Function to calculate GC content
def calculate_gc_content(sequence):
    sequence = sequence.upper()
    gc_count = sequence.count('G') + sequence.count('C')
    total_bases = len(sequence)
    return (gc_count / total_bases) * 100 if total_bases > 0 else 0

# Function for heart rate analysis
def analyze_heart_rate(heart_rate):
    if heart_rate < 60:
        return "Bradycardia (Heart rate is too slow)", """
        **Treatments and Precautions:**
        - **Medications:** Beta-blockers, calcium channel blockers, and antiarrhythmic drugs.
        - **Pacemaker:** A device implanted to regulate slow heart rhythms.
        - **Lifestyle Changes:** Avoid excessive alcohol and caffeine, maintain a healthy diet, and engage in regular physical activity.
        - **Regular Monitoring:** Keep track of your heart rate and consult your doctor regularly.
        """
    elif 60 <= heart_rate <= 100:
        return "Normal Heart Rate", """
        **General Precautions:**
        - Maintain a heart-healthy diet rich in fruits, vegetables, and whole grains.
        - Avoid excessive caffeine, alcohol, and smoking.
        - Manage stress through meditation, yoga, or deep breathing exercises.
        - Engage in regular physical activity but avoid overexertion.
        - Monitor and control conditions such as high blood pressure, diabetes, and sleep apnea.
        - Follow prescribed medications and medical advice.
        """
    else:
        return "Tachycardia (Heart rate is too fast)", """
        **Treatments and Precautions:**
        - **Medications:** Beta-blockers, calcium channel blockers, and antiarrhythmic drugs.
        - **Cardioversion:** Electrical shock therapy used to restore normal heart rhythm.
        - **Catheter Ablation:** A minimally invasive procedure that destroys the heart tissue causing abnormal electrical signals.
        - **Lifestyle Changes:** Avoid triggers such as stress, caffeine, and alcohol.
        - **Regular Monitoring:** Keep track of your heart rate and consult your doctor regularly.
        """

# Function for Amino Acid to DNA and RNA Conversion (Updated to handle sequences)
def amino_acid_to_dna_rna(amino_acid_sequence):
    amino_to_codon = {
        'A': ['GCT', 'GCC', 'GCA', 'GCG'],
        'C': ['TGT', 'TGC'],
        'D': ['GAT', 'GAC'],
        'E': ['GAA', 'GAG'],
        'F': ['TTT', 'TTC'],
        'G': ['GGT', 'GGC', 'GGA', 'GGG'],
        'H': ['CAT', 'CAC'],
        'I': ['ATT', 'ATC', 'ATA'],
        'K': ['AAA', 'AAG'],
        'L': ['TTA', 'TTG', 'CTT', 'CTC', 'CTA', 'CTG'],
        'M': ['ATG'],
        'N': ['AAT', 'AAC'],
        'P': ['CCT', 'CCC', 'CCA', 'CCG'],
        'Q': ['CAA', 'CAG'],
        'R': ['CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],
        'S': ['TCT', 'TCC', 'TCA', 'TCG', 'AGT', 'AGC'],
        'T': ['ACT', 'ACC', 'ACA', 'ACG'],
        'V': ['GTT', 'GTC', 'GTA', 'GTG'],
        'W': ['TGG'],
        'Y': ['TAT', 'TAC'],
        '*': ['TAA', 'TAG', 'TGA']
    }
    
    # Initialize an empty list to store the codons for the sequence
    codons_sequence = []
    
    for amino_acid in amino_acid_sequence.upper():
        if amino_acid in amino_to_codon:
            codons_sequence.append(amino_to_codon[amino_acid])
        else:
            codons_sequence.append(['Unknown'])  # If the amino acid is not recognized, append 'Unknown'

    return codons_sequence

# Improved Navigation with Icons in Main Taskbar
selected_option = option_menu(
    menu_title="      ❤️ ARRHYTHMIA DATAHUB AND TOOLS        ",
    options=[
        "Arrhythmia Overview",
        "Arrhythmia Database",
        "GC Content",
        "Heart Rate",
        "Amino Acid to DNA/RNA",
        "Full Database"  
    ],
    icons=["heartbeat", "database", "dna", "heart", "dna", "table"],  # Updated icon list
    menu_icon="menu",
    default_index=0,
    orientation="horizontal"
)

# Application Sections
if selected_option == "Arrhythmia Overview":
    st.markdown('<div class="three-d-heading">❤️ Arrhythmia </div>', unsafe_allow_html=True)
    st.write(
        "Arrhythmias are irregularities in heartbeat that can be too fast (tachycardia), too slow (bradycardia), or erratic. "
        "These irregular heart rhythms occur due to disruptions in the electrical signals controlling the heartbeat. "
        "Arrhythmias can be harmless or life-threatening, depending on the type and severity."
    )

    st.write("### Types of Arrhythmia")
    image_path = r"arrhythmia image.jpg"
    st.image(image_path, caption="Arrhythmia Classification", use_container_width=True)
    st.markdown(
        "- **Atrial Fibrillation (AFib):** A rapid, irregular heartbeat originating in the atria. It increases the risk of stroke."
        "\n- **Atrial Flutter:** Similar to AFib but with a more organized rhythm."
        "\n- **Supraventricular Tachycardia (SVT):** A rapid heartbeat originating above the ventricles."
        "\n- **Ventricular Tachycardia:** A fast, regular heart rate arising from the ventricles, which can be life-threatening."
        "\n- **Ventricular Fibrillation:** A chaotic heart rhythm that requires immediate medical intervention."
        "\n- **Bradycardia:** A slow heart rate, often caused by issues in the sinoatrial node or conduction system."
        "\n- **Heart Block:** A delay or blockage in the electrical signals that regulate the heart."
    )

    st.write("### Precautions and Lifestyle Changes")
    st.markdown(
        "- Maintain a heart-healthy diet rich in fruits, vegetables, and whole grains."
        "\n- Avoid excessive caffeine, alcohol, and smoking."
        "\n- Manage stress through meditation, yoga, or deep breathing exercises."
        "\n- Engage in regular physical activity but avoid overexertion."
        "\n- Monitor and control conditions such as high blood pressure, diabetes, and sleep apnea."
        "\n- Follow prescribed medications and medical advice."
    )

    st.write("### Treatments")
    st.markdown(
        "- **Medications:** Beta-blockers, calcium channel blockers, anticoagulants, and antiarrhythmic drugs."
        "\n- **Lifestyle Changes:** Adopting a healthy diet, exercising, and avoiding arrhythmia triggers."
        "\n- **Pacemakers:** Devices implanted to regulate slow heart rhythms."
        "\n- **Implantable Cardioverter Defibrillator (ICD):** A device used to prevent sudden cardiac arrest in high-risk patients."
        "\n- **Cardioversion:** Electrical shock therapy used to restore normal heart rhythm."
        "\n- **Catheter Ablation:** A minimally invasive procedure that destroys the heart tissue causing abnormal electrical signals."
        "\n- **Surgery:** In severe cases, procedures like maze surgery may be performed to correct arrhythmia."
    )

    st.write("### Conclusion")
    st.write(
        "Arrhythmias range from harmless to life-threatening conditions. Early detection, lifestyle modifications, and appropriate medical interventions "
        "can significantly improve quality of life and prevent complications. Regular check-ups and adherence to medical advice are essential for managing arrhythmia."
    )
elif selected_option == "Arrhythmia Database":
    st.markdown('<div class="three-d-heading">🧬 Arrhythmia Gene Search</div>', unsafe_allow_html=True)
    data = load_data()
    if data is not None:
        gene_name = st.text_input("Enter Gene Name:")
        if gene_name:
            filtered_data = data[data["Gene Names"].str.contains(gene_name, case=False, na=False)]
            if not filtered_data.empty:
                filtered_data = filtered_data.copy()
                if "Gene Links" in filtered_data.columns:
                    filtered_data["Gene Names"] = filtered_data.apply(
                        lambda row: f'<a href="{row["Gene Links"]}" target="_blank">{row["Gene Names"]}</a>'
                        if row["Gene Links"] else row["Gene Names"], axis=1)
                if "Sequence" in filtered_data.columns:
                    filtered_data["Sequence"] = filtered_data["Sequence"].apply(
                        lambda x: f'<a href="{x}" target="_blank">View Sequence</a>' if pd.notna(x) else "N/A")
                if "pubmed" in filtered_data.columns:
                    filtered_data["pubmed"] = filtered_data["pubmed"].apply(
                        lambda x: f'<a href="{x}" target="_blank">View pubmed</a>' if pd.notna(x) else "N/A")
                st.write(filtered_data.to_html(escape=False, index=False), unsafe_allow_html=True)
            else:
                st.write("No gene found with the provided name.")

elif selected_option == "GC Content":
    st.markdown('<div class="three-d-heading">🧪 GC Content Calculator</div>', unsafe_allow_html=True)
    fasta_sequence = st.text_area("Paste your sequence here:")
    if st.button("Calculate GC Content"):
        sequence = ''.join([line for line in fasta_sequence.splitlines() if not line.startswith('>')])
        gc_content = calculate_gc_content(sequence)
        st.write(f"### GC Content: {gc_content:.2f}%")


elif selected_option == "Heart Rate":
    st.markdown('<div class="three-d-heading">💓 Heart Rate Analysis</div>', unsafe_allow_html=True)
    heart_rate = st.number_input("Enter your heart rate (beats per minute):", min_value=0, step=1)
    if st.button("Analyze Heart Rate"):
        result, precautions = analyze_heart_rate(heart_rate)
        st.write(f"### Result: {result}")
        st.write(precautions)

elif selected_option == "Amino Acid to DNA/RNA":
    st.markdown('<div class="three-d-heading">🔬 Amino Acid to DNA/RNA</div>', unsafe_allow_html=True)
    amino_acid_sequence = st.text_input("Enter Amino Acid Sequence (e.g., MKTG):").strip()
    if st.button("Convert"):
        if amino_acid_sequence:
            codons_sequence = amino_acid_to_dna_rna(amino_acid_sequence)
            codons_str = [', '.join(codons) for codons in codons_sequence]
            st.write(f"### DNA/RNA Codons for the Sequence:")
            st.write(", ".join(codons_str))
        else:
            st.write("Please enter a valid amino acid sequence.")

elif selected_option == "Full Database":
    st.markdown('<div class="three-d-heading">📘 Full Arrhythmia Database</div>', unsafe_allow_html=True)
    data = load_data()
    if data is not None:
        if "Sequence" in data.columns:
            data["Sequence"] = data["Sequence"].apply(
                lambda x: f'<a href="{x}" target="_blank">View Sequence</a>' if pd.notna(x) else "N/A")
        if "pubmed" in data.columns:
            data["pubmed"] = data["pubmed"].apply(
                lambda x: f'<a href="{x}" target="_blank">View in pubmed</a>' if pd.notna(x) else "N/A")
        st.write(data.to_html(escape=False, index=False), unsafe_allow_html=True)
