"""
Script to generate the complete Microsoft Word report (.docx) and export the PDF
for Analysis of Algorithms Assignment: "Empirical Analysis of Sorting Algorithms".

Student: Arslan Tahir
SAP ID: 47120
Subject: Analysis of Algorithms
Repository: https://github.com/sapid47120/Sorting_Algorithm_Analysis
"""

import os
import csv
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

BASE_DIR = r"C:\Users\Arslan\Desktop\Assingment no 3\Sorting_Algorithm_Analysis"
RESULTS_DIR = os.path.join(BASE_DIR, "results")
PLOTS_DIR = os.path.join(BASE_DIR, "plots")
SUBMISSION_DIR = os.path.join(BASE_DIR, "submission")
os.makedirs(SUBMISSION_DIR, exist_ok=True)

DOCX_PATH = os.path.join(SUBMISSION_DIR, "47120_ArslanTahir_SortingAnalysis.docx")
PDF_PATH = os.path.join(SUBMISSION_DIR, "47120_ArslanTahir_SortingAnalysis.pdf")
REPO_URL = "https://github.com/sapid47120/Fall26AoA2026"


from docx.opc.constants import RELATIONSHIP_TYPE


def add_hyperlink(paragraph, url, text, color="2B6CB0", underline=True):
    """Inserts a real, clickable hyperlink into a python-docx paragraph."""
    part = paragraph.part
    r_id = part.relate_to(url, RELATIONSHIP_TYPE.HYPERLINK, is_external=True)

    hyperlink = parse_xml(f'<w:hyperlink {nsdecls("w")} {nsdecls("r")} r:id="{r_id}"/>')
    new_run = parse_xml(f'<w:r {nsdecls("w")}/>')
    rPr = parse_xml(f'<w:rPr {nsdecls("w")}/>')

    if color:
        c = parse_xml(f'<w:color {nsdecls("w")} w:val="{color}"/>')
        rPr.append(c)
    if underline:
        u = parse_xml(f'<w:u {nsdecls("w")} w:val="single"/>')
        rPr.append(u)

    rPr.append(parse_xml(f'<w:rFonts {nsdecls("w")} w:ascii="Calibri" w:hAnsi="Calibri"/>'))
    new_run.append(rPr)
    new_run.text = text
    hyperlink.append(new_run)
    paragraph._p.append(hyperlink)
    return hyperlink


def set_cell_background(cell, fill_hex):
    """Sets background color of a table cell."""
    tcPr = cell._element.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    tcPr.append(shd)


def set_table_borders(table):
    """Applies clean, subtle borders to a table."""
    tblPr = table._element.xpath('w:tblPr')
    if tblPr:
        borders = parse_xml(
            f'<w:tblBorders {nsdecls("w")}>'
            f'  <w:top w:val="single" w:sz="6" w:space="0" w:color="CCCCCC"/>'
            f'  <w:bottom w:val="single" w:sz="8" w:space="0" w:color="1A365D"/>'
            f'  <w:insideH w:val="single" w:sz="4" w:space="0" w:color="E2E8F0"/>'
            f'  <w:insideV w:val="none"/>'
            f'  <w:left w:val="none"/>'
            f'  <w:right w:val="none"/>'
            f'</w:tblBorders>'
        )
        tblPr[0].append(borders)


def add_page_number_to_section(section):
    """Adds a page number field in the section footer."""
    footer = section.footer
    p = footer.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    run = p.add_run("Page ")
    run.font.name = "Calibri"
    run.font.size = Pt(9)
    run.font.color.rgb = RGBColor(113, 128, 150)

    fldSimple = OxmlElement('w:fldSimple')
    fldSimple.set(qn('w:instr'), 'PAGE')
    p._p.append(fldSimple)

    run2 = p.add_run(" of ")
    run2.font.name = "Calibri"
    run2.font.size = Pt(9)
    run2.font.color.rgb = RGBColor(113, 128, 150)

    fldSimple2 = OxmlElement('w:fldSimple')
    fldSimple2.set(qn('w:instr'), 'NUMPAGES')
    p._p.append(fldSimple2)


def read_csv_data(filepath):
    rows = []
    with open(filepath, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for r in reader:
            rows.append(r)
    return rows


def build_docx_report():
    doc = Document()

    # 1-inch margins
    for s in doc.sections:
        s.top_margin = Inches(1.0)
        s.bottom_margin = Inches(1.0)
        s.left_margin = Inches(1.0)
        s.right_margin = Inches(1.0)

    navy = RGBColor(26, 54, 93)        # #1A365D Deep Navy
    slate = RGBColor(43, 108, 176)     # #2B6CB0 Blue
    charcoal = RGBColor(45, 55, 72)    # #2D3748 Body text

    # Normal Style
    style_normal = doc.styles['Normal']
    style_normal.font.name = 'Calibri'
    style_normal.font.size = Pt(11)
    style_normal.font.color.rgb = charcoal
    style_normal.paragraph_format.line_spacing = 1.15
    style_normal.paragraph_format.space_after = Pt(6)

    # ==========================================
    # 1. TITLE PAGE
    # ==========================================
    p_pre = doc.add_paragraph()
    p_pre.paragraph_format.space_before = Pt(48)
    p_pre.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_pre = p_pre.add_run("UNIVERSITY ASSIGNMENT REPORT")
    r_pre.font.size = Pt(12)
    r_pre.font.bold = True
    r_pre.font.color.rgb = slate

    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title.paragraph_format.space_after = Pt(16)
    r_title = p_title.add_run("Empirical Analysis of Sorting Algorithms")
    r_title.font.size = Pt(26)
    r_title.font.bold = True
    r_title.font.color.rgb = navy

    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_sub.paragraph_format.space_after = Pt(48)
    r_sub = p_sub.add_run("Comparative Performance Study on Bubble Sort, Selection Sort,\nInsertion Sort, and Merge Sort Across Varying Input Sizes")
    r_sub.font.size = Pt(13)
    r_sub.font.italic = True
    r_sub.font.color.rgb = RGBColor(74, 85, 104)

    # Student Details Box
    table_meta = doc.add_table(rows=5, cols=2)
    table_meta.alignment = WD_TABLE_ALIGNMENT.CENTER
    meta_info = [
        ("Student Name:", "Arslan Tahir"),
        ("SAP ID:", "47120"),
        ("Subject:", "Analysis of Algorithms"),
        ("Date:", "November 2026"),
        ("GitHub Repository:", REPO_URL),
    ]
    for row_idx, (k, v) in enumerate(meta_info):
        row = table_meta.rows[row_idx]
        cell_k, cell_v = row.cells[0], row.cells[1]

        p_k = cell_k.paragraphs[0]
        p_k.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        r_k = p_k.add_run(k)
        r_k.font.bold = True
        r_k.font.color.rgb = navy

        p_v = cell_v.paragraphs[0]
        if k == "GitHub Repository:":
            add_hyperlink(p_v, v, v, color="2B6CB0", underline=True)
        else:
            r_v = p_v.add_run(v)
            r_v.font.color.rgb = charcoal

        cell_k.width = Inches(2.2)
        cell_v.width = Inches(3.8)

    doc.add_page_break()

    # Footer page numbering
    body_section = doc.sections[-1]
    add_page_number_to_section(body_section)

    def add_heading_1(text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(16)
        p.paragraph_format.space_after = Pt(6)
        p.paragraph_format.keep_with_next = True
        run = p.add_run(text)
        run.font.size = Pt(16)
        run.font.bold = True
        run.font.color.rgb = navy
        return p

    def add_heading_2(text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(12)
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.keep_with_next = True
        run = p.add_run(text)
        run.font.size = Pt(13)
        run.font.bold = True
        run.font.color.rgb = slate
        return p

    # ==========================================
    # 2. INTRODUCTION
    # ==========================================
    add_heading_1("1. Introduction")
    doc.add_paragraph(
        "Sorting is one of the most fundamental operations in computer science. It organizes a collection of items into a "
        "defined order (such as ascending or descending). Efficient sorting is critical for optimizing other algorithms, "
        "such as binary searching and database indexing. While theoretical asymptotic analysis (Big-O notation) provides "
        "a mathematical upper bound on algorithm scaling, real-world execution time is influenced by constant factors, "
        "memory movement, implementation language, and processor architecture."
    )
    doc.add_paragraph(
        "This project carries out an empirical performance analysis of four foundational sorting algorithms: Bubble Sort, "
        "Selection Sort, Insertion Sort, and Merge Sort. Each algorithm is implemented from scratch in pure Python without "
        "relying on built-in sorting functions. Execution times are measured across both pre-sorted (ascending) and reverse-ordered "
        "(descending) inputs for sizes N = 5, 10, 50, and 100 to evaluate best-case, average-case, and worst-case behaviors."
    )

    # ==========================================
    # 3. OBJECTIVES
    # ==========================================
    add_heading_1("2. Objectives")
    objectives = [
        "Implement four sorting algorithms (Bubble Sort, Selection Sort, Insertion Sort, and Merge Sort) from scratch in pure Python.",
        "Test each algorithm on the exact four ascending input arrays specified in the assignment: N = 5, 10, 50, and 100.",
        "Generate descending-order (reverse-sorted) test inputs to evaluate worst-case performance under maximum inversions.",
        "Accurately measure execution time using high-precision hardware timers (time.perf_counter_ns()).",
        "Perform at least 5 independent benchmark runs with 500 internal repetitions per run to eliminate clock noise on small arrays.",
        "Ensure input array immutability so that sorting routines do not mutate original input data.",
        "Visualize execution trends with Matplotlib line charts and compare empirical growth rates directly with theoretical time complexities."
    ]
    for obj in objectives:
        p = doc.add_paragraph(style='List Bullet')
        p.paragraph_format.space_after = Pt(3)
        p.add_run(obj)

    # ==========================================
    # 4. METHODOLOGY
    # ==========================================
    add_heading_1("3. Methodology")

    add_heading_2("3.1 Algorithm Implementations")
    doc.add_paragraph(
        "All algorithms were written from scratch in Python and designed to return a sorted copy while preserving the original input:"
    )

    algos_desc = [
        ("Bubble Sort: ", "Repeatedly steps through the list, compares adjacent elements, and swaps them if they are out of order. An early-exit flag ('swapped') is included: if a complete pass occurs with zero swaps, the algorithm terminates immediately. This provides an optimal O(N) best-case execution time on already sorted arrays, while retaining O(N^2) worst-case time on reverse-ordered data."),
        ("Selection Sort: ", "Divides the array into a sorted prefix and an unsorted suffix. In each pass, it scans the unsorted portion to find the minimum element and performs at most one swap to place it at the beginning of the unsorted segment. Because it always performs N(N-1)/2 comparisons regardless of initial element ordering, its time complexity is strictly O(N^2) in all cases."),
        ("Insertion Sort: ", "Builds the sorted array one element at a time. It iterates through the array and inserts each element into its proper position in the already-sorted portion by shifting larger items to the right. On pre-sorted inputs, it requires only one comparison per element and zero shifts (O(N) best case). On reverse-ordered inputs, each element must be shifted past all preceding elements, yielding O(N^2) worst-case time."),
        ("Merge Sort: ", "A divide-and-conquer algorithm that recursively splits the input array into two equal halves until sub-arrays of size 1 remain, then merges the sorted halves using a two-pointer technique. It guarantees O(N log N) time complexity across best, average, and worst cases, at the cost of O(N) auxiliary memory for sub-array allocations.")
    ]
    for name, desc in algos_desc:
        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(4)
        r1 = p.add_run(name)
        r1.bold = True
        r1.font.color.rgb = navy
        p.add_run(desc)

    add_heading_2("3.2 Test Datasets")
    doc.add_paragraph(
        "The assignment specifies four exact ascending arrays representing increasing problem sizes:"
    )
    arrays_text = [
        "Arr1 (N = 5): {1, 2, 3, 4, 5}",
        "Arr2 (N = 10): {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}",
        "Arr3 (N = 50): {1, 2, 3, ..., 49, 50}",
        "Arr4 (N = 100): {1, 2, 3, ..., 99, 100}"
    ]
    for arr_t in arrays_text:
        p = doc.add_paragraph(style='List Bullet')
        p.paragraph_format.space_after = Pt(2)
        r = p.add_run(arr_t)
        r.font.name = 'Consolas'
        r.font.size = Pt(10)

    doc.add_paragraph(
        "To evaluate worst-case behavior, descending test arrays were generated for the identical sizes (N = 5, 10, 50, 100) "
        "as {N, N-1, ..., 1}. Reverse ordering maximizes inversions (exactly N(N-1)/2 inverted pairs), which forces Bubble Sort "
        "and Insertion Sort to execute their theoretical maximum operations."
    )

    add_heading_2("3.3 High-Precision Timing & Experimental Control")
    doc.add_paragraph(
        "Measuring operations that execute in microseconds on modern CPUs requires rigorous experimental controls to prevent "
        "timing inaccuracies:"
    )
    method_points = [
        ("High-Resolution Timer: ", "Python's time.perf_counter_ns() was used, which accesses hardware performance counters with nanosecond-level resolution, avoiding low-precision system clock quantization."),
        ("Pre-allocation of Test Copies: ", "All test arrays were copied prior to entering the timed loop. This strictly isolates the sorting algorithm's execution time from Python list creation or memory allocation overhead."),
        ("Multi-Run Repetition: ", "Because an individual sort of N=5 takes under 2 microseconds, each measurement pass executed 500 repetitions in an inner loop. Total elapsed nanoseconds were divided by 500 and converted to microseconds (us)."),
        ("Statistical Averaging: ", "Five independent benchmark runs were conducted for every algorithm and input size combination, and the arithmetic mean across all 5 runs was reported."),
        ("Garbage Collection Management: ", "Python's automatic garbage collection was explicitly triggered (gc.collect()) and temporarily disabled (gc.disable()) during the timed measurement loop, eliminating random latency spikes from background collection cycles.")
    ]
    for title_m, desc_m in method_points:
        p = doc.add_paragraph(style='List Bullet')
        p.paragraph_format.space_after = Pt(3)
        r = p.add_run(title_m)
        r.bold = True
        p.add_run(desc_m)

    # ==========================================
    # 5. RESULTS
    # ==========================================
    doc.add_page_break()
    add_heading_1("4. Empirical Results")
    doc.add_paragraph(
        "The benchmark was executed using the methodology described above. The tables below present the actual measured "
        "average execution times in microseconds (us) for both ascending and descending inputs across 5 runs of 500 repetitions."
    )

    # Ascending Results Table
    asc_csv_path = os.path.join(RESULTS_DIR, "ascending_benchmark_results.csv")
    asc_rows = read_csv_data(asc_csv_path)

    p_tbl1 = doc.add_paragraph()
    p_tbl1.paragraph_format.space_before = Pt(10)
    p_tbl1.paragraph_format.space_after = Pt(4)
    r_tbl1 = p_tbl1.add_run("Table 1: Average Execution Times for Ascending Inputs (μs) - Best / Typical Case")
    r_tbl1.bold = True
    r_tbl1.font.color.rgb = navy

    table_asc = doc.add_table(rows=len(asc_rows), cols=5)
    table_asc.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(table_asc)

    for r_idx, row_data in enumerate(asc_rows):
        row = table_asc.rows[r_idx]
        for c_idx, val in enumerate(row_data):
            cell = row.cells[c_idx]
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.RIGHT if c_idx > 0 else WD_ALIGN_PARAGRAPH.CENTER
            if r_idx == 0:
                set_cell_background(cell, "1A365D")
                run = p.add_run(val if c_idx == 0 else f"{val} (μs)")
                run.bold = True
                run.font.color.rgb = RGBColor(255, 255, 255)
            else:
                if r_idx % 2 == 1:
                    set_cell_background(cell, "F7FAFC")
                run = p.add_run(f"{float(val):.4f}" if c_idx > 0 else str(val))
                run.font.color.rgb = charcoal
            cell.width = Inches(1.25)

    doc.add_paragraph().paragraph_format.space_after = Pt(12)

    # Descending Results Table
    desc_csv_path = os.path.join(RESULTS_DIR, "descending_benchmark_results.csv")
    desc_rows = read_csv_data(desc_csv_path)

    p_tbl2 = doc.add_paragraph()
    p_tbl2.paragraph_format.space_before = Pt(8)
    p_tbl2.paragraph_format.space_after = Pt(4)
    r_tbl2 = p_tbl2.add_run("Table 2: Average Execution Times for Descending Inputs (μs) - Worst Case")
    r_tbl2.bold = True
    r_tbl2.font.color.rgb = navy

    table_desc = doc.add_table(rows=len(desc_rows), cols=5)
    table_desc.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(table_desc)

    for r_idx, row_data in enumerate(desc_rows):
        row = table_desc.rows[r_idx]
        for c_idx, val in enumerate(row_data):
            cell = row.cells[c_idx]
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.RIGHT if c_idx > 0 else WD_ALIGN_PARAGRAPH.CENTER
            if r_idx == 0:
                set_cell_background(cell, "1A365D")
                run = p.add_run(val if c_idx == 0 else f"{val} (μs)")
                run.bold = True
                run.font.color.rgb = RGBColor(255, 255, 255)
            else:
                if r_idx % 2 == 1:
                    set_cell_background(cell, "F7FAFC")
                run = p.add_run(f"{float(val):.4f}" if c_idx > 0 else str(val))
                run.font.color.rgb = charcoal
            cell.width = Inches(1.25)

    # ==========================================
    # 6. GRAPHS
    # ==========================================
    doc.add_page_break()
    add_heading_1("5. Graphical Analysis")
    doc.add_paragraph(
        "Execution-time graphs were generated using Matplotlib based directly on the empirical results in Tables 1 and 2. "
        "The X-axis shows the input size N, and the Y-axis shows the average execution time in microseconds (us)."
    )

    asc_plot_path = os.path.join(PLOTS_DIR, "execution_time_ascending.png")
    if os.path.exists(asc_plot_path):
        p_img1 = doc.add_paragraph()
        p_img1.alignment = WD_ALIGN_PARAGRAPH.CENTER
        doc.add_picture(asc_plot_path, width=Inches(5.8))

        p_cap1 = doc.add_paragraph()
        p_cap1.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_cap1.paragraph_format.space_after = Pt(10)
        r_cap1 = p_cap1.add_run("Figure 1: Average Execution Time vs. Input Size N on Ascending (Pre-Sorted) Arrays.")
        r_cap1.font.size = Pt(9.5)
        r_cap1.font.bold = True
        r_cap1.font.color.rgb = navy

        doc.add_paragraph(
            "Graph Explanation (Figure 1): On pre-sorted inputs, Bubble Sort and Insertion Sort scale almost linearly "
            "(15.46 us and 16.68 us at N=100) because their inner loops exit after confirming sorted order. Selection Sort "
            "exhibits a steep quadratic curve reaching 366.26 us at N=100 because it always scans the entire remaining sub-array. "
            "Merge Sort scales moderately according to its O(N log N) curve, reaching 264.98 us."
        )

    desc_plot_path = os.path.join(PLOTS_DIR, "execution_time_descending.png")
    if os.path.exists(desc_plot_path):
        p_img2 = doc.add_paragraph()
        p_img2.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img2.paragraph_format.space_before = Pt(8)
        doc.add_picture(desc_plot_path, width=Inches(5.8))

        p_cap2 = doc.add_paragraph()
        p_cap2.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_cap2.paragraph_format.space_after = Pt(10)
        r_cap2 = p_cap2.add_run("Figure 2: Average Execution Time vs. Input Size N on Descending (Worst-Case) Arrays.")
        r_cap2.font.size = Pt(9.5)
        r_cap2.font.bold = True
        r_cap2.font.color.rgb = navy

        doc.add_paragraph(
            "Graph Explanation (Figure 2): On reverse-ordered inputs, Bubble Sort (1135.89 us) and Insertion Sort (627.77 us) "
            "display prominent quadratic growth due to maximum element swaps and shifts. Selection Sort (403.67 us) also exhibits "
            "quadratic growth. In contrast, Merge Sort (124.21 us) maintains superior O(N log N) scaling, emerging as the fastest "
            "algorithm at N=100 by a substantial margin."
        )

    # ==========================================
    # 7. ANALYSIS AND DISCUSSION
    # ==========================================
    doc.add_page_break()
    add_heading_1("6. Analysis and Discussion")

    add_heading_2("6.1 Theoretical vs. Empirical Growth Comparison")
    doc.add_paragraph(
        "To verify whether empirical behavior matches theoretical asymptotic complexity, we observe the growth multiplier "
        "when doubling the problem size from N = 50 to N = 100:"
    )

    table_growth = doc.add_table(rows=5, cols=4)
    table_growth.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(table_growth)

    growth_headers = ["Algorithm", "Theoretical Factor", "Ascending Growth (N: 50→100)", "Descending Growth (N: 50→100)"]
    growth_data = [
        ("Bubble Sort", "4.0x (Worst) / 2.0x (Best)", "1.75x (near linear)", "4.66x (quadratic)"),
        ("Selection Sort", "4.0x (All cases)", "5.24x (quadratic)", "3.20x (quadratic)"),
        ("Insertion Sort", "4.0x (Worst) / 2.0x (Best)", "2.03x (exact linear)", "3.87x (near theoretical 4.0x)"),
        ("Merge Sort", "2.35x (N log N)", "2.88x (linearithmic)", "1.35x (sub-linearithmic)")
    ]
    for c_idx, h in enumerate(growth_headers):
        cell = table_growth.rows[0].cells[c_idx]
        set_cell_background(cell, "1A365D")
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run(h)
        run.bold = True
        run.font.color.rgb = RGBColor(255, 255, 255)

    for r_idx, row_vals in enumerate(growth_data):
        row = table_growth.rows[r_idx + 1]
        for c_idx, val in enumerate(row_vals):
            cell = row.cells[c_idx]
            if (r_idx + 1) % 2 == 1:
                set_cell_background(cell, "F7FAFC")
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER if c_idx > 0 else WD_ALIGN_PARAGRAPH.LEFT
            run = p.add_run(val)
            run.font.color.rgb = charcoal

    doc.add_paragraph().paragraph_format.space_after = Pt(8)

    add_heading_2("6.2 Best-Case vs. Worst-Case Behavior")
    doc.add_paragraph(
        "1. Bubble Sort: On ascending inputs, Bubble Sort's swapped flag detects ordered data in a single pass of N-1 "
        "comparisons, yielding 15.46 us at N=100. On descending inputs, every pair is inverted, requiring N(N-1)/2 swaps, "
        "causing runtime to surge to 1135.89 us (a 73-fold increase)."
    )
    doc.add_paragraph(
        "2. Insertion Sort: Displays exceptional best-case efficiency (16.68 us at N=100 on ascending inputs) with an "
        "exact 2.03x scaling from N=50 to 100, perfectly matching O(N) theory. In the worst case (descending), each key "
        "must be shifted across the entire sorted prefix, driving runtime up to 627.77 us (37x slower)."
    )
    doc.add_paragraph(
        "3. Selection Sort: Shows virtually identical quadratic curves for both ascending (366.26 us) and descending (403.67 us) "
        "inputs. This confirms the theoretical property that Selection Sort is data-insensitive: it unconditionally searches the entire "
        "remaining list for the minimum value, executing exactly N(N-1)/2 comparisons in every scenario."
    )
    doc.add_paragraph(
        "4. Merge Sort: Demonstrates robust O(N log N) consistency. On descending inputs at N=100, Merge Sort is the fastest "
        "algorithm (124.21 us), executing over 9 times faster than Bubble Sort and 5 times faster than Insertion Sort."
    )

    add_heading_2("6.3 Observed Deviations and Measurement Overhead")
    doc.add_paragraph(
        "For small input sizes (N = 5 and N = 10), two minor deviations from simple asymptotic models were observed:"
    )
    anomalies = [
        ("Constant-Factor Overhead in Merge Sort: ", "At N = 5 and N = 10, Merge Sort is slower than the iterative quadratic algorithms (7.53 us for Merge Sort vs. 1.77 us for Bubble Sort at N=5). This is expected in practical computing: Merge Sort incurs recursive function call overhead, stack frame creation, and dynamic sub-list allocation. These constant factors dominate for tiny inputs, but as N reaches 50 and 100, its O(N log N) asymptotic efficiency easily overcomes the overhead."),
        ("Interpreter and Loop Dispatch Overhead: ", "In Python, each loop iteration and dictionary lookup carries bytecode dispatch overhead. For tiny arrays (N = 5), the execution time reflects Python's loop setup as much as the comparison logic itself. Repeating each measurement 500 times with disabled garbage collection effectively smoothed this noise.")
    ]
    for anom_t, anom_d in anomalies:
        p = doc.add_paragraph(style='List Bullet')
        p.paragraph_format.space_after = Pt(4)
        r = p.add_run(anom_t)
        r.bold = True
        p.add_run(anom_d)

    # ==========================================
    # 8. CONCLUSION
    # ==========================================
    add_heading_1("7. Conclusion")
    doc.add_paragraph(
        "This empirical analysis successfully demonstrates the practical performance profiles of Bubble Sort, Selection Sort, "
        "Insertion Sort, and Merge Sort:"
    )
    conclusions = [
        "Insertion Sort is the most efficient choice for pre-sorted or nearly sorted data, running in O(N) time with minimal constant overhead.",
        "Bubble Sort with an early-exit flag achieves O(N) best-case performance on sorted data, but degrades into the slowest algorithm in the worst case (1135.89 us at N=100) due to intensive pairwise swapping.",
        "Selection Sort provides predictable O(N^2) performance regardless of initial array ordering, but is consistently outperformed by Insertion Sort on sorted inputs and by Merge Sort on large reverse-ordered inputs.",
        "Merge Sort validates asymptotic algorithmic theory: while recursive overhead makes it slower on very small arrays (N <= 10), its O(N log N) divide-and-conquer strategy makes it significantly superior as input size scales, outperforming all quadratic algorithms by 3x to 9x at N = 100 in the worst case."
    ]
    for c in conclusions:
        p = doc.add_paragraph(style='List Bullet')
        p.paragraph_format.space_after = Pt(3)
        p.add_run(c)

    # ==========================================
    # 9. GITHUB REPOSITORY LINK (Section 8)
    # ==========================================
    add_heading_1("8. GitHub Repository Link")
    doc.add_paragraph(
        "The complete source code, benchmark suite, unit tests, and generated assets are publicly accessible in the project repository:"
    )
    p_link = doc.add_paragraph()
    p_link.paragraph_format.space_before = Pt(6)
    p_link.paragraph_format.space_after = Pt(12)
    r_link_lbl = p_link.add_run("GitHub Repository URL: ")
    r_link_lbl.bold = True
    add_hyperlink(p_link, REPO_URL, REPO_URL, color="2B6CB0", underline=True)

    doc.save(DOCX_PATH)
    print(f"Generated Word document successfully: {DOCX_PATH}")


if __name__ == "__main__":
    build_docx_report()
