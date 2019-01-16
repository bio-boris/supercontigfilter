/*
A KBase module: bsadkhinContigFilter
This sample module contains one small method that filters contigs.
*/

module bsadkhinContigFilter {
    typedef structure {
        string report_name;
        string report_ref;
    } ReportResults;

    /*
        This example function accepts any number of parameters and returns results in a KBaseReport
    */
    funcdef run_bsadkhinContigFilter(mapping<string,UnspecifiedObject> params) returns (ReportResults output) authentication required;

    funcdef run_bsadkhinContigFilter_max(mapping<string,UnspecifiedObject> params) returns (ReportResults output) authentication required;

};
