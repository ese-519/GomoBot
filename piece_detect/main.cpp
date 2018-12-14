
#include "opencv2/opencv.hpp"
#include <iostream>
#include <string>
using namespace cv;
using namespace std;

class Gomoku_detection{
private:
	// images
	Mat im_with_keypoints;
	Mat im_inv;	
	Mat im;

	// Storage for blobs
	vector<KeyPoint> keypoints;
	vector<KeyPoint> keypoints_inv;

	// Setup SimpleBlobDetector parameters.
	SimpleBlobDetector::Params params;

public:
	Gomoku_detection(){
		cout<<"The detection object in being called"<<endl;

		// Change thresholds
		params.minThreshold = 0;
		params.maxThreshold = 255;

		// Filter by Area.
		params.filterByArea = true;
		params.minArea = 100;

		// Filter by Circularity
		params.filterByCircularity = true;
		params.minCircularity = 0.5;

		// Filter by Convexity
		params.filterByConvexity = true;
		params.minConvexity = 0.85;

		// Filter by Inertia
		params.filterByInertia = true;
		params.minInertiaRatio = 0.01;

	}

	void read_image(string address){
		// Read image
		im = imread(address, IMREAD_GRAYSCALE );
		// Mat im = imread( "3.jpg", CV_LOAD_IMAGE_COLOR );
		threshold(im, im_inv, 200, 255, THRESH_BINARY_INV);
	}

	int piece_detection(){

		#if CV_MAJOR_VERSION < 3   // If you are using OpenCV 2

			// Set up detector with params
			SimpleBlobDetector detector(params);

			// Detect blobs
			detector.detect( im, keypoints);
			detector.detect( im_inv, keypoints_inv);
		#else 

			// Set up detector with params
			Ptr<SimpleBlobDetector> detector = SimpleBlobDetector::create(params);   

			// Detect blobs
			detector->detect( im, keypoints);
			detector->detect( im_inv, keypoints_inv);
		#endif 

		// Draw detected blobs as red circles.
		// DrawMatchesFlags::DRAW_RICH_KEYPOINTS flag ensures
		// the size of the circle corresponds to the size of blob
		for (int i=0; i<keypoints.size(); i++){ 
			cout << keypoints[i].pt.x << " " << keypoints[i].pt.y<<endl ;
		}

		for (int i=0; i<keypoints_inv.size(); i++){ 
			keypoints.push_back(keypoints_inv[i]);
			cout << keypoints_inv[i].pt.x << " " << keypoints_inv[i].pt.y<<endl ;
		}

		drawKeypoints(im, keypoints, im_with_keypoints, Scalar(0,0,255), DrawMatchesFlags::DRAW_RICH_KEYPOINTS );
		// drawKeypoints( im_inv, keypoints_inv, im_with_keypoints, Scalar(0,0,255), DrawMatchesFlags::DRAW_RICH_KEYPOINTS );

		// Show blobs
		namedWindow("Display window", WINDOW_NORMAL);
		imshow("Display window", im_with_keypoints );
		cout.flush();
		waitKey(0);
	}
};

int main( int argc, char** argv )
{
	cout << "hello"<<endl;
	// Build the object
	Gomoku_detection dec;
	dec.read_image("black.jpg");
	dec.piece_detection();	
	cout.flush();
	waitKey(0);
}