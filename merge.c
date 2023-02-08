c for merge sort
 §§ --- 0x1B-sorting_algorithms/103-merge_sort.c
 §§ 1000
+#include "sort.h"
+
+/**
+ * merge_sort - sorts an array of integers in ascending order
+ * @array: integer array
+ * @size: size of array
+ *
+ */
+
+void merge_sort(int *array, size_t size)
+{
+	if (array == NULL || size < 2)
+		return;
+
+	merge_split(array, size);
+}
+
+/**
+ * merge_split - splits array into two halves
+ * @array: integer array
+ * @size: size of array
+ *
+ */
+
+void merge_split(int *array, size_t size)
+{
+	size_t mid;
+	int *left, *right;
+
+	if (size < 2)
+		return;
+
+	mid = size / 2;
+	left = array;
+	right = array + mid;
+
+	merge_split(left, mid);
+	merge_split(right, size - mid);
+	merge(array, size, mid, left, right);
+}
+
+/**
+ * merge - merges two subarrays back into one
+ * @array: integer array
+ * @size: size of array
+ * @mid: midpoint of array
+ * @left: left side of array
+ * @right: right side of array
+ *
+ */
+
+void merge(int *array, size_t size, size_t mid, int *left, int *right)
+{
+	int *temp, *left_end, *right_end;
+	size_t left_size = mid;
+	size_t right_size = size - mid;
+	size_t i = 0, j = 0, k = 0;
+
+	left_end = left + left_size;
+	right_end = right + right_size;
+	temp = malloc(sizeof(int) * size);
+
+	if (temp == NULL)
+		return;
+
+	while (left < left_end && right < right_end)
+	{
+		if (*left <= *right)
+			temp[k++] = *(left++);
+		else
+			temp[k++] = *(right++);
+	}
+
+	while (left < left_end)
+		temp[k++] = *(left++);
+
+	while (right < right_end)
+		temp[k++] = *(right++);
+
+	for (i = 0; i < size; i++)
+	{
+		array[I] = temp[i];
+	}
+
+	free(temp);
+	print_array(array, size);
+}
