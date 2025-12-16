def readfile(filename):
    try:
        with open(filename,'r')as f:
            content=f.read()
            return content
    except FileNotFoundError:
        return "!!!File Not found!!!"

def analyze_logs(text):
    lines=text.splitlines()
    Total_Line=len(lines)
    error_count=0
    warning_count=0
    for line in lines:
        line_lower=line.lower()
        if "info" in line_lower:
            continue
        if "error" in line_lower:
            error_count+=1
        if "warning"in line_lower:
            warning_count+=1
    return{"Lines:":Total_Line,
                "Error:":error_count,
                "Warning:":warning_count}

def write_report(analysis_results,output_filename):
    try:
        with open(output_filename,'w')as f:
            f.write("Lines: " + str(analysis_results["Lines:"]) + "\n")
            f.write("Error: " + str(analysis_results["Error:"]) + "\n")
            f.write("Warning: " + str(analysis_results["Warning:"]) + "\n")
        return "Report written successfully"

    except FileNotFoundError:
        return "File is missing"

def main():
    filepath=input("Enter the path of log file:")
    log_content=readfile(filepath)
    if log_content=="!!!File not found!!!":
        print("The file could not be found.\n" \
        " Exiting the program")
        return
    analysis_results=analyze_logs(log_content)
    write_report(analysis_results,"report.txt")
    print("Report has been written to report.txt sucessfully")


if __name__=="__main__":
    main()








            
